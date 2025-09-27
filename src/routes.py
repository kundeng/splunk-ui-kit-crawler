"""
Route handlers for different types of Splunk UI Kit pages.

This module defines specialized handlers for:
- Package index pages
- Package overview pages  
- Component documentation pages
- General fallback handler
"""

import logging
from urllib.parse import urlparse
from datetime import datetime
from pathlib import Path

from crawlee.crawlers import PlaywrightCrawlingContext
from crawlee.router import Router

from markdown_exporter import MarkdownExporter
from tab_processor import discover_tabs, switch_to_tab, click_show_code_buttons, extract_tab_content
from code_extractor import extract_code_blocks_from_html, extract_props_from_html, extract_text_content

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
    
    # Wait for the SPA to load main content with more patience
    try:
        await context.page.wait_for_selector('main', timeout=30_000)
        logger.info('Main content found, waiting for network idle...')
        await context.page.wait_for_load_state('networkidle', timeout=15_000)
        logger.info('Network idle achieved, waiting additional time for JavaScript...')
        await context.page.wait_for_timeout(1000)  # Reduced from 3000ms
    except Exception as e:
        logger.warning(f'Timeout waiting for content on {context.request.url}: {e}')
        # Try to continue anyway
    
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
    
    # Process tabs and extract content
    main_content = ''
    code_blocks = []
    props = []
    exploration = {
        'available_tabs': [],
        'tabs_clicked': [],
        'toggles_clicked': [],
        'tab_contents': {},
    }
    
    try:
        # Discover available tabs
        available_tabs = await discover_tabs(context)
        exploration['available_tabs'] = available_tabs
        
        # Process each tab
        for tab_name in available_tabs:
            try:
                # Switch to the tab
                if await switch_to_tab(context, tab_name):
                    exploration['tabs_clicked'].append(tab_name)
                    
                    # Extract content immediately after switching
                    tab_content = await extract_tab_content(context, tab_name)
                    tab_text = f'## {tab_name}\n\n{tab_content}\n\n' if tab_content else f'## {tab_name}\n\n'
                    
                    # Only click "Show code" buttons and extract code from Examples tab
                    if 'examples' in tab_name.lower():
                        tab_code_blocks = await click_show_code_buttons(context, tab_name)
                        if tab_code_blocks:
                            code_blocks.extend(tab_code_blocks)
                            exploration['toggles_clicked'].extend(['Show code'] * len(tab_code_blocks))
                            
                            # Add code blocks to Examples section
                            for i, code_text in enumerate(tab_code_blocks):
                                language = 'jsx' if ('import React' in code_text or 'export default' in code_text) else 'javascript'
                                tab_text += f'\n### Example {i + 1}\n\n```{language}\n{code_text}\n```\n'
                    
                    main_content += tab_text
                    
            except Exception as e:
                logger.warning(f'Error processing tab {tab_name}: {e}')
                continue
                
    except Exception as e:
        logger.warning(f'Error during tab processing: {e}')
    
    # Log results
    if code_blocks:
        logger.info(f'Found {len(code_blocks)} code blocks on {url}')
        
        # Convert extracted code blocks to the expected format
        formatted_code_blocks = []
        for i, code_text in enumerate(code_blocks):
            # Detect language from content patterns
            language = 'text'
            if 'import React' in code_text or 'export default' in code_text or 'jsx' in code_text.lower():
                language = 'jsx'
            elif 'function' in code_text and '{' in code_text:
                language = 'javascript'
            elif 'class=' in code_text and '<' in code_text:
                language = 'jsx'
            
            formatted_code_blocks.append({
                'language': language,
                'code': code_text
            })
            logger.info(f'Formatted code block {i+1}: {language}, {len(code_text)} chars')
        
        code_blocks = formatted_code_blocks
    else:
        logger.warning(f'No code blocks found on {url}')
        
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
        
        # Give minimal time for interactive examples to render
        await context.page.wait_for_timeout(500)  # Reduced from 3000ms
        
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
