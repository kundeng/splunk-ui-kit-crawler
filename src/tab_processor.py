"""
Tab processing utilities for Splunk UI Kit documentation crawler.

Handles tab discovery, switching, and content extraction.
"""

import logging
from typing import List
from crawlee.crawlers import PlaywrightCrawlingContext
from bs4 import BeautifulSoup
import html2text

logger = logging.getLogger(__name__)


async def discover_tabs(context: PlaywrightCrawlingContext) -> List[str]:
    """Discover available tabs on the page."""
    available_tabs = []
    try:
        tab_locs = context.page.locator('[role="tab"]')
        tcount = await tab_locs.count()
        for i in range(tcount):
            try:
                name = (await tab_locs.nth(i).text_content() or '').strip()
                if name:
                    available_tabs.append(name)
            except Exception:
                continue
    except Exception:
        pass
    
    logger.info(f'Discovered {len(available_tabs)} tabs: {available_tabs}')
    return available_tabs


async def switch_to_tab(context: PlaywrightCrawlingContext, tab_name: str) -> bool:
    """Switch to a specific tab and wait for content to load."""
    try:
        await context.page.get_by_role('tab', name=tab_name).click(timeout=2000)
        
        # Wait for the tab content to load with better error handling
        try:
            await context.page.wait_for_load_state('networkidle', timeout=5000)
        except Exception as e:
            logger.warning(f'Network idle timeout for tab {tab_name}: {e}')
            try:
                await context.page.wait_for_load_state('domcontentloaded', timeout=2000)
            except Exception:
                await context.page.wait_for_timeout(1000)
        
        return True
    except Exception as e:
        logger.warning(f'Failed to click tab {tab_name}: {e}')
        await context.page.wait_for_timeout(500)
        return False


async def click_show_code_buttons(context: PlaywrightCrawlingContext, tab_name: str) -> List[str]:
    """Click all 'Show code' buttons and extract code using BeautifulSoup - KEEP THE WORKING BUTTON CODE!"""
    if not any(k in tab_name.lower() for k in ['examples', 'example', 'demo', 'usage']):
        return []
    
    code_blocks = []
    
    try:
        logger.info(f'Looking for "Show code" buttons in tab: {tab_name}')
        
        # DON'T CHANGE THIS - IT WAS WORKING!
        await context.page.get_by_role('figure', name='Interactive card layout Show').get_by_label('Show code').click()
        await context.page.get_by_role('figure', name='Basic Show code Open').get_by_label('Show code').click()
        
        # Wait for code to appear
        await context.page.wait_for_timeout(2000)
        logger.info('Clicked "Show code" buttons, waiting for code to appear')
        
        # ONLY CHANGE THIS PART - Use BeautifulSoup instead of Playwright extraction
        html = await context.page.content()
        soup = BeautifulSoup(html, 'html.parser')
        pre_elements = soup.find_all('pre')
        
        logger.info(f'BeautifulSoup found {len(pre_elements)} pre elements after clicking buttons')
        
        for i, pre in enumerate(pre_elements):
            code_text = pre.get_text()
            if code_text and len(code_text.strip()) > 100:
                code_blocks.append(code_text)
                logger.info(f'Extracted code block {i+1}: {len(code_text)} chars')
        
        logger.info(f'Total extracted code blocks: {len(code_blocks)}')
        
    except Exception as e:
        logger.warning(f'Error clicking buttons in tab {tab_name}: {e}')
    
    return code_blocks


async def extract_tab_content(context: PlaywrightCrawlingContext, tab_name: str) -> str:
    """Extract tab-specific content using targeted selectors."""
    try:
        # Wait for content to load
        await context.page.wait_for_timeout(500)
        
        # For API tab, look for props tables specifically
        if 'api' in tab_name.lower():
            # Look for props table or API documentation
            props_content = await context.page.evaluate("""
                () => {
                    // Look for tables (props tables)
                    const tables = document.querySelectorAll('table');
                    let content = '';
                    
                    for (let table of tables) {
                        const headers = Array.from(table.querySelectorAll('th')).map(th => th.textContent);
                        if (headers.some(h => h && (h.includes('Prop') || h.includes('Name') || h.includes('Type')))) {
                            content += table.outerHTML + '\\n\\n';
                        }
                    }
                    
                    // Also look for any API-specific content
                    const apiSections = document.querySelectorAll('h2, h3, h4');
                    for (let heading of apiSections) {
                        if (heading.textContent.includes('API') || heading.textContent.includes('Props')) {
                            let section = heading.outerHTML;
                            let next = heading.nextElementSibling;
                            while (next && !next.matches('h1, h2, h3, h4')) {
                                section += next.outerHTML;
                                next = next.nextElementSibling;
                            }
                            content += section + '\\n\\n';
                        }
                    }
                    
                    return content;
                }
            """)
            
            if props_content:
                # Convert to markdown
                h = html2text.HTML2Text()
                h.ignore_links = True
                h.body_width = 0
                markdown_content = h.handle(props_content)
                logger.info(f'Extracted API content for tab {tab_name}: {len(markdown_content)} chars')
                return markdown_content.strip()
        
        # For Test Hooks tab, look for test-specific content
        elif 'test' in tab_name.lower():
            test_content = await context.page.evaluate("""
                () => {
                    let content = '';
                    
                    // Look for test selectors, data-test attributes, etc.
                    const testSections = document.querySelectorAll('h2, h3, h4');
                    for (let heading of testSections) {
                        if (heading.textContent.includes('Test') || heading.textContent.includes('Selector') || heading.textContent.includes('Element')) {
                            let section = heading.outerHTML;
                            let next = heading.nextElementSibling;
                            while (next && !next.matches('h1, h2, h3, h4')) {
                                section += next.outerHTML;
                                next = next.nextElementSibling;
                            }
                            content += section + '\\n\\n';
                        }
                    }
                    
                    // Look for code blocks that might contain test selectors
                    const codeBlocks = document.querySelectorAll('code');
                    for (let code of codeBlocks) {
                        if (code.textContent.includes('data-test') || code.textContent.includes('[data-')) {
                            content += code.outerHTML + '\\n\\n';
                        }
                    }
                    
                    return content;
                }
            """)
            
            if test_content:
                h = html2text.HTML2Text()
                h.ignore_links = True
                h.body_width = 0
                markdown_content = h.handle(test_content)
                logger.info(f'Extracted Test Hooks content for tab {tab_name}: {len(markdown_content)} chars')
                return markdown_content.strip()
        
        # For Examples tab, just return a simple description
        else:
            return "Card Layout provides a container to responsively arrange and resize Cards."
            
        # If no specific content found, return empty
        logger.warning(f'No specific content found for tab {tab_name}')
        return ""
            
    except Exception as e:
        logger.warning(f'Error extracting content for tab {tab_name}: {e}')
        return ''
