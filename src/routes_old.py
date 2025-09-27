"""
Route handlers for different types of Splunk UI Kit pages.

This module defines specialized handlers for:
- Package index pages
- Package overview pages  
- Component documentation pages
- General fallback handler
"""

import logging
import re
from urllib.parse import urlparse, unquote
from datetime import datetime
from pathlib import Path

from bs4 import BeautifulSoup

from markdown_exporter import MarkdownExporter

from crawlee.crawlers import PlaywrightCrawlingContext
from crawlee.router import Router

logger = logging.getLogger(__name__)

# Create the router instance
router = Router[PlaywrightCrawlingContext]()

# Initialize a module-level Markdown exporter for streaming writes
_DOCS_DIR = Path(__file__).parent.parent / "docs"
_exporter = MarkdownExporter(_DOCS_DIR)


@router.default_handler
async def default_handler(context: PlaywrightCrawlingContext) -> None:
    """
    Default handler for all pages. Handles SPA content loading and basic extraction.
    """
    logger.info(f'Processing: {context.request.url}')
    
    # Wait for the SPA to load main content
    try:
        await context.page.wait_for_selector('main', timeout=30_000)
        await context.page.wait_for_load_state('networkidle', timeout=10_000)
    except Exception as e:
        logger.warning(f'Timeout waiting for content on {context.request.url}: {e}')
    
    # Extract basic page information
    url = context.request.url
    title = await context.page.title() or 'Untitled'
    
    # Parse URL to determine page type and metadata
    parsed_url = urlparse(url)
    path_parts = [p for p in parsed_url.path.split('/') if p]
    
    page_type = 'unknown'
    package_name = None
    component = None
    
    if len(path_parts) >= 1 and path_parts[0] == 'Packages':
        if len(path_parts) == 1:
            page_type = 'packages_index'
        elif len(path_parts) == 2:
            page_type = 'package_overview'
            package_name = path_parts[1]
        elif len(path_parts) == 3:
            page_type = 'component'
            package_name = path_parts[1]
            component = path_parts[2]
        elif len(path_parts) >= 3:
            page_type = 'component'
            package_name = path_parts[1]
            component = path_parts[2]
    
    # Try to expose examples and API content broadly before extraction (exploration phase)
    exploration = {
        'available_tabs': [],
        'tabs_clicked': [],
        'toggles_clicked': [],
        'tab_contents': {},  # Store HTML per tab
    }
    try:
        # Discover available tabs
        try:
            tab_locs = context.page.locator('[role="tab"]')
            tcount = await tab_locs.count()
            for i in range(tcount):
                try:
                    name = (await tab_locs.nth(i).text_content() or '').strip()
                    if name:
                        exploration['available_tabs'].append(name)
                except Exception:
                    continue
        except Exception:
            pass

        # Extract content for each tab
        for tab_name in exploration['available_tabs']:
                # Click the tab
                try:
                    await context.page.get_by_role('tab', name=tab_name).click(timeout=2000)
                    exploration['tabs_clicked'].append(tab_name)
                    
                    # Wait for the tab content to load with better error handling
                    try:
                        # First try to wait for network to be idle (best case)
                        await context.page.wait_for_load_state('networkidle', timeout=5000)
                    except Exception as e:
                        logger.warning(f'Network idle timeout for tab {tab_name}, using fallback wait: {e}')
                        # Fallback: wait for DOM content to be loaded
                        try:
                            await context.page.wait_for_load_state('domcontentloaded', timeout=2000)
                        except Exception:
                            # Last resort: just wait a bit
                            await context.page.wait_for_timeout(1000)
                except Exception as e:
                    logger.warning(f'Failed to click tab {tab_name}: {e}')
                    # Try to recover by waiting a bit
                    await context.page.wait_for_timeout(500)
                    continue
                
                # Extract main HTML after tab switch
                tab_html = ''
                try:
                    main_el = await context.page.query_selector('main')
                    if main_el:
                        tab_html = await main_el.inner_html()
                except Exception:
                    pass
                exploration['tab_contents'][tab_name] = tab_html
                
                # Perform interactions for this tab (toggles, scroll)
                # Click code toggles if examples-related
                if any(k in tab_name.lower() for k in ['examples', 'example', 'demo', 'usage']):
                    try:
                        # Log the tab we're working on
                        logger.info(f'Looking for code buttons in tab: {tab_name}')
                        
                        # Use more specific selectors for the "Show code" buttons
                        button_selectors = [
                            'button:has-text("Show code")', 
                            '[role="button"]:has-text("Show code")',
                            'button:has-text("show code")',
                            '[role="button"]:has-text("show code")',
                            'button, [role="button"]'  # Fallback to generic buttons
                        ]
                        
                        # Try each selector
                        for selector in button_selectors:
                            btns = context.page.locator(selector)
                            bcount = await btns.count()
                            logger.info(f'Found {bcount} buttons with selector: {selector}')
                            
                            if bcount > 0:
                                break
                        
                        # Process all found buttons
                        for i in range(bcount):
                            try:
                                el = btns.nth(i)
                                name = (await el.text_content() or '').strip()
                                aria = (await el.get_attribute('aria-label') or '').strip()
                                label = name or aria
                                if label and re.search(r"^(show|hide)\s*code$", label, re.I):
                                    # Log before clicking
                                    logger.info(f'Clicking "{label}" button')
                                    
                                    # Use a try-except block to handle potential context destroyed errors
                                    try:
                                        # Click the button
                                        await el.click(timeout=900)
                                        exploration['toggles_clicked'].append(label)
                                        
                                        # First wait for any network activity to settle
                                        try:
                                            await context.page.wait_for_load_state('networkidle', timeout=1000)
                                        except Exception:
                                            # If that fails, just wait a bit
                                            await context.page.wait_for_timeout(300)
                                        
                                        # Wait for the code block to appear after clicking
                                        try:
                                            # First try to find the parent figure element
                                            figure_element = el.locator('xpath=./ancestor::figure')
                                            # Wait for a pre tag to be visible within it
                                            await figure_element.locator('pre').wait_for(timeout=2000)
                                            logger.info(f'Code block revealed and visible for "{label}"')
                                            
                                            # After confirming visibility, wait longer for syntax highlighting to complete
                                            await context.page.wait_for_timeout(1000)
                                        except Exception as e:
                                            logger.warning(f'Could not find revealed code block in figure for "{label}": {e}')
                                            
                                            # Try a different approach - wait for any pre tag to appear
                                            try:
                                                await context.page.wait_for_selector('pre', timeout=2000)
                                                logger.info(f'Found pre tag after clicking "{label}"')
                                                await context.page.wait_for_timeout(1000)
                                            except Exception as e2:
                                                logger.warning(f'Could not find any pre tag: {e2}')
                                                
                                                # Try specific selectors for Splunk UI Kit code blocks
                                                try:
                                                    await context.page.wait_for_selector('.TransitionOpenStyles__StyledInner-sc-1x58s0g-1', timeout=2000)
                                                    logger.info(f'Found TransitionOpenStyles container after clicking "{label}"')
                                                    await context.page.wait_for_timeout(1000)
                                                except Exception as e3:
                                                    logger.warning(f'Could not find any code container: {e3}')
                                                    await context.page.wait_for_timeout(1500) # Even longer fallback wait
                                    except Exception as e:
                                        logger.warning(f'Error clicking button or waiting for code: {e}')
                                        await context.page.wait_for_timeout(1000) # Wait a bit to recover
                            except Exception as e:
                                logger.warning(f'Error processing button {i}: {e}')
                                continue
                    except Exception as e:
                        logger.warning(f'Error processing buttons on tab {tab_name}: {e}')
                
                # Re-extract HTML after interactions with better error handling
                try:
                    # Wait a bit more to ensure all code blocks are fully rendered
                    await context.page.wait_for_timeout(500)
                    
                    # First try to get the main element
                    main_el = await context.page.query_selector('main')
                    if main_el:
                        try:
                            # Get the inner HTML with a longer timeout
                            tab_html = await main_el.inner_html(timeout=5000)
                            logger.info(f'Re-extracted HTML for tab {tab_name}: {len(tab_html)} chars')
                            
                            # Check if we have code blocks in the HTML
                            if 'pre' in tab_html or 'code' in tab_html:
                                logger.info(f'Tab {tab_name} HTML contains code tags')
                            
                            # Store the HTML
                            exploration['tab_contents'][tab_name] = tab_html
                        except Exception as e:
                            logger.warning(f'Error getting inner HTML: {e}')
                    else:
                        logger.warning('Main element not found for re-extraction')
                except Exception as e:
                    logger.warning(f'Error re-extracting HTML after interactions: {e}')
                    # Keep the previous HTML if we failed to get a new one
                    if tab_name not in exploration['tab_contents'] or not exploration['tab_contents'][tab_name]:
                        exploration['tab_contents'][tab_name] = '<!-- Failed to extract HTML -->'
                        logger.warning('Using empty placeholder for tab HTML')
                
    except Exception:
        pass

    # Process tab contents with BeautifulSoup to extract clean text and code
    main_content = ''
    code_blocks = []
    props = []
    
    for tab_name, html in exploration['tab_contents'].items():
        if html.strip():
            try:
                soup = BeautifulSoup(html, 'html.parser')
                
                # Remove images to avoid clutter
                for img in soup.find_all('img'):
                    img.decompose()
                
                # Extract code blocks before removing them - try multiple selectors
                code_elements = []
                
                # Try different selectors for code blocks - ordered by specificity
                selectors_to_try = [
                    # Specific selectors for Splunk UI Kit code blocks
                    'pre.CodeStyles__StyledPre-sc-1eq4k68-1',           # Exact class from Splunk UI Kit
                    'pre.DocExampleStyles__StyledCode-sc-1628k2t-1',    # Another exact class
                    'code.CodeStyles__StyledCode-sc-1eq4k68-0',         # Exact code class
                    'code.language-jsx',                                # JSX language code
                    '.TransitionOpenStyles__StyledInner-sc-1x58s0g-1 pre', # Parent container for revealed code
                    
                    # More general selectors as fallbacks
                    'figure pre',                   # Pre tags inside figures
                    'figure pre code',              # Code blocks inside figures
                    'pre.language-jsx',             # JSX language pre
                    'pre.language-javascript',       # JavaScript language pre
                    'pre.language-typescript',       # TypeScript language pre
                    'code[class*="language-"]',    # Any language code
                    'pre code',                     # Code inside pre tags
                    'pre',                          # Pre tags themselves
                    '[class*="code"]',             # Elements with "code" in class name
                ]
                
                for selector in selectors_to_try:
                    elements = soup.select(selector)
                    if elements:
                        code_elements.extend(elements)
                        logger.info(f'Tab {tab_name}: Selector "{selector}" found {len(elements)} elements')
                
                # Filter out duplicates while preserving order
                seen = set()
                unique_code_elements = []
                for el in code_elements:
                    # Use element's string representation as a hash
                    el_hash = str(el)
                    if el_hash not in seen:
                        seen.add(el_hash)
                        unique_code_elements.append(el)
                code_elements = unique_code_elements
                logger.info(f'Tab {tab_name}: Total unique code elements: {len(code_elements)}')
                
                for code_element in code_elements:
                    # Get text with whitespace preserved for code formatting
                    code_text = code_element.get_text()
                    
                    # Log detailed info about the code element
                    element_classes = code_element.get("class", [])
                    parent_classes = code_element.parent.get("class", []) if code_element.parent else []
                    logger.info(f'Code element: {len(code_text)} chars, classes: {element_classes}, parent classes: {parent_classes}')
                    
                    # Preserve formatting but remove excessive whitespace
                    lines = code_text.splitlines()
                    
                    # Remove common leading whitespace (dedent)
                    if lines:
                        non_empty_lines = [line for line in lines if line.strip()]
                        if non_empty_lines:
                            min_indent = min(len(line) - len(line.lstrip()) for line in non_empty_lines)
                            lines = [line[min_indent:] if line.strip() else line for line in lines]
                    
                    # Rejoin with consistent line endings
                    code_text = "\n".join(lines)
                    
                    # Only include code blocks with sufficient content
                    if code_text and len(code_text.strip()) > 20:  # Lowered threshold to catch more code
                        # Detect language
                        classes = code_element.get('class', []) or []
                        language = 'text'
                        for cls in classes:
                            if cls.startswith('language-'):
                                language = cls.replace('language-', '')
                                break
                        if 'javascript' in classes or 'js' in classes:
                            language = 'javascript'
                        elif 'typescript' in classes or 'ts' in classes:
                            language = 'typescript'
                        elif 'json' in classes:
                            language = 'json'
                        elif 'jsx' in classes:
                            language = 'jsx'
                        
                        code_blocks.append({
                            'language': language,
                            'code': code_text
                        })
                        logger.info(f'Added code block: {language}, {len(code_text)} chars')
                
                # Extract props from API tab
                if 'api' in tab_name.lower():
                    tables = soup.find_all('table')
                    for table in tables:
                        tbody = table.find('tbody')
                        if not tbody:
                            continue
                        headers = []
                        thead = table.find('thead')
                        if thead:
                            headers = [th.get_text(strip=True).lower() for th in thead.find_all('th')]
                        else:
                            first_row = tbody.find('tr')
                            if first_row:
                                headers = [td.get_text(strip=True).lower() for td in first_row.find_all(['td', 'th'])]
                        
                        if not any(h in headers for h in ['prop', 'name', 'type']):
                            continue
                        
                        rows = tbody.find_all('tr')
                        start_i = 1 if not thead and rows else 0
                        for i, row in enumerate(rows):
                            if i < start_i:
                                continue
                            cells = row.find_all(['td', 'th'])
                            if not cells:
                                continue
                            prop_obj = {
                                'name': cells[0].get_text(strip=True) if len(cells) > 0 else '',
                                'type': cells[1].get_text(strip=True) if len(cells) > 1 else '',
                                'default': cells[2].get_text(strip=True) if len(cells) > 2 else '',
                                'description': cells[3].get_text(strip=True) if len(cells) > 3 else '',
                            }
                            if any(prop_obj.values()):
                                props.append(prop_obj)
                
                # Get clean text content for this tab
                tab_text = soup.get_text(separator='\n', strip=True)
                if tab_text:
                    main_content += f'## {tab_name}\n\n{tab_text}\n\n'
                    
            except Exception as e:
                logger.warning(f'Failed to process tab {tab_name}: {e}')

    # Brief visibility for iteration when focusing a single page
    if code_blocks:
        logger.info(f'Found {len(code_blocks)} code blocks on {url}')
    if props:
        logger.info(f'Found {len(props)} props on {url}')
    
    # Create structured data for export
    page_data = {
        'title': title,
        'url': url,
        'type': page_type,
        'package': package_name,
        'component': component,
        'content': main_content,
        'code_blocks': code_blocks,
        'props': props,
        'exploration': exploration,
        'crawled_at': datetime.now().isoformat(),
    }
    
    # Stream export to Markdown per page to reduce memory pressure
    try:
        await _exporter.export_page(page_data)
    except Exception as e:
        logger.warning(f'Streaming export failed for {url}: {e}')
    
    # Enqueue links for further crawling
    try:
        await context.enqueue_links(
            strategy='same-domain',
            selector='nav a[href]:not([href^="mailto:"]):not([href^="tel:"]), main a[href]:not([href^="mailto:"]):not([href^="tel:"]), article a[href]:not([href^="mailto:"]):not([href^="tel:"])',
        )
    except Exception as e:
        logger.warning(f'Failed to enqueue links from {url}: {e}')


@router.handler('packages_index')
async def packages_index_handler(context: PlaywrightCrawlingContext) -> None:
    """Handler specifically for the main packages index page."""
    logger.info(f'Processing packages index: {context.request.url}')
    
    # Use the default handler but with specific focus on package links
    await default_handler(context)
    
    # Additionally, try to find and enqueue all package links
    try:
        package_links = await context.page.query_selector_all('article a[href*="/Packages/"]')
        for link in package_links:
            href = await link.get_attribute('href')
            if href and href.startswith('/'):
                # Convert relative URLs to absolute
                full_url = f"https://splunkui.splunk.com{href}"
                await context.add_requests([full_url])
    except Exception as e:
        logger.warning(f'Failed to enqueue package links: {e}')


@router.handler('component')
async def component_handler(context: PlaywrightCrawlingContext) -> None:
    """Handler specifically for component documentation pages."""
    logger.info(f'Processing component page: {context.request.url}')
    
    # Wait for component examples to load with better error handling
    try:
        # First wait for the page to be fully loaded
        try:
            await context.page.wait_for_load_state('networkidle', timeout=10_000)
        except Exception as e:
            logger.warning(f'Network idle timeout for component page: {e}')
            # Fallback to domcontentloaded
            try:
                await context.page.wait_for_load_state('domcontentloaded', timeout=5_000)
            except Exception:
                pass
        
        # Then wait for the main content to be available
        try:
            await context.page.wait_for_selector('main', timeout=30_000)
            logger.info('Main content found')
        except Exception as e:
            logger.warning(f'Main content selector timeout: {e}')
        
        # Give extra time for interactive examples to render
        await context.page.wait_for_timeout(3000)
        
        # Check if tabs are available and log them
        try:
            tabs = await context.page.query_selector_all('[role="tab"]')
            tab_count = len(tabs)
            logger.info(f'Found {tab_count} tabs on the component page')
        except Exception as e:
            logger.warning(f'Error checking tabs: {e}')
            
    except Exception as e:
        logger.warning(f'Error during component page preparation: {e}')

    # Delegate to default handler which performs exploration and extraction
    try:
        await default_handler(context)
    except Exception as e:
        logger.error(f'Error in default_handler for component page: {e}')
        # Try to recover by taking a screenshot if possible
        try:
            screenshot_path = f"/tmp/error-{datetime.now().strftime('%Y%m%d-%H%M%S')}.png"
            await context.page.screenshot(path=screenshot_path)
            logger.info(f'Error screenshot saved to {screenshot_path}')
        except Exception:
            pass
