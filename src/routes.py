"""
Clean route handlers for Splunk UI Kit pages.
"""

import logging
from urllib.parse import urlparse
from datetime import datetime
from pathlib import Path
import html2text

from crawlee.crawlers import PlaywrightCrawlingContext
from crawlee.router import Router

from markdown_exporter import MarkdownExporter
from tab_processor import discover_tabs, switch_to_tab, click_show_code_buttons, extract_tab_content

logger = logging.getLogger(__name__)

# Create the router instance
router = Router[PlaywrightCrawlingContext]()

# Initialize a module-level Markdown exporter for streaming writes
_DOCS_DIR = Path(__file__).parent.parent / "docs"
_exporter = MarkdownExporter(_DOCS_DIR)


async def handle_component_page(context: PlaywrightCrawlingContext) -> tuple[str, list]:
    """Handle component pages with tabs (Button, Table, Modal, etc.)"""
    main_content = ''
    code_blocks = []
    
    # Discover and process tabs
    available_tabs = await discover_tabs(context)
    logger.info(f'Found {len(available_tabs)} tabs: {available_tabs}')
    
    for tab_name in available_tabs:
        if await switch_to_tab(context, tab_name):
            # Extract content
            tab_content = await extract_tab_content(context, tab_name)
            main_content += f'## {tab_name}\n\n{tab_content}\n\n'
            
            # Click show code buttons for Examples tab
            if 'examples' in tab_name.lower():
                tab_code_blocks = await click_show_code_buttons(context, tab_name)
                code_blocks.extend(tab_code_blocks)
    
    return main_content, code_blocks


async def handle_package_docs_page(context: PlaywrightCrawlingContext) -> tuple[str, list]:
    """Handle package documentation pages (@splunk/create, etc.)"""
    # Just extract main content - no tabs
    main_element = context.page.locator('main')
    if await main_element.count() > 0:
        main_html = await main_element.inner_html()
        
        h = html2text.HTML2Text()
        h.ignore_links = False
        h.ignore_images = True
        main_content = h.handle(main_html)
        
        logger.info(f'Extracted main content: {len(main_content)} chars')
        return main_content, []
    else:
        logger.warning('No main element found')
        return "<!-- No main content found -->", []


@router.default_handler
async def default_handler(context: PlaywrightCrawlingContext) -> None:
    """Clean handler with proper page type detection."""
    logger.info(f'Processing: {context.request.url}')
    
    # Wait for the SPA to load with better error handling
    try:
        await context.page.wait_for_selector('main', timeout=30_000)
        await context.page.wait_for_load_state('networkidle', timeout=15_000)
        await context.page.wait_for_timeout(500)  # Minimal wait
    except Exception as e:
        logger.error(f'CRITICAL: Failed to load page {context.request.url}: {e}')
        # Stop crawling on context destruction errors
        if 'context was destroyed' in str(e).lower():
            logger.error('Context destruction detected - stopping crawler')
            raise e
        logger.warning(f'Timeout waiting for content: {e}')
    
    # Extract basic page information with error handling
    try:
        url = context.request.url
        title = await context.page.title() or 'Untitled'
    except Exception as e:
        logger.error(f'CRITICAL: Failed to get page info for {context.request.url}: {e}')
        raise e
    
    # Parse URL to determine page type
    parsed_url = urlparse(url)
    path_parts = [p for p in parsed_url.path.split('/') if p]
    
    # CORRECT PAGE TYPE DETECTION with error handling
    try:
        if '/react-ui/' in url and len(path_parts) >= 3:
            # Component pages: Button, Table, Modal, etc. (have tabs)
            page_type = 'component'
            package_name = 'react-ui'
            component = path_parts[2]
            
            logger.info(f'Handling component page: {component}')
            main_content, code_blocks = await handle_component_page(context)
            
        else:
            # ALL other package pages: create, themes, dashboard-docs, etc.
            page_type = 'package_docs'
            package_name = path_parts[1] if len(path_parts) >= 2 else 'unknown'
            component = path_parts[2] if len(path_parts) >= 3 else None
            
            logger.info(f'Handling package docs page: {package_name}/{component}')
            main_content, code_blocks = await handle_package_docs_page(context)
    except Exception as e:
        logger.error(f'CRITICAL: Content extraction failed for {url}: {e}')
        raise e
    
    # Log results
    if code_blocks:
        logger.info(f'Found {len(code_blocks)} code blocks')
    else:
        logger.warning(f'No code blocks found on {url}')
    
    # Create structured data for export
    page_data = {
        'title': title,
        'url': url,
        'type': page_type,
        'package': package_name,
        'component': component,
        'content': main_content,
        'code_blocks': code_blocks,
        'crawled_at': datetime.now().isoformat()
    }
    
    # Export to markdown
    await _exporter.export_page(page_data)
    
    # ENABLE AUTO-DISCOVERY: Enqueue links found on this page
    await context.enqueue_links()
