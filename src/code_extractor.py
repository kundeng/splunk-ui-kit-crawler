"""
Code block extraction utilities for Splunk UI Kit crawler.
"""

import logging
from typing import Dict, List, Any
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)


def extract_code_blocks_from_html(html: str, tab_name: str) -> List[Dict[str, Any]]:
    """Extract code blocks from HTML content - simplified approach."""
    if not html.strip():
        return []
    
    code_blocks = []
    
    # If we have content from Playwright direct extraction, treat it as code
    if html and len(html.strip()) > 50:
        # Split by double newlines to separate different code blocks
        blocks = html.split('\n\n')
        
        for i, block in enumerate(blocks):
            block = block.strip()
            if len(block) > 50:  # Only substantial code blocks
                # Detect language from content patterns
                language = 'text'
                if 'import React' in block or 'export default' in block or 'jsx' in block.lower():
                    language = 'jsx'
                elif 'function' in block and '{' in block:
                    language = 'javascript'
                elif 'class=' in block and '<' in block:
                    language = 'jsx'
                
                code_blocks.append({
                    'language': language,
                    'code': block
                })
                logger.info(f'Tab {tab_name}: Added code block {i+1}: {language}, {len(block)} chars')
    
    logger.info(f'Tab {tab_name}: Extracted {len(code_blocks)} total code blocks')
    return code_blocks


def extract_props_from_html(html: str, tab_name: str) -> List[Dict[str, Any]]:
    """Extract props table from API tab HTML."""
    if not html.strip() or 'api' not in tab_name.lower():
        return []
    
    # For now, skip props extraction to avoid BeautifulSoup mess
    # TODO: Use Playwright to extract props table directly
    logger.info(f'Skipping props extraction for {tab_name} - needs Playwright implementation')
    return []


def extract_text_content(html: str, tab_name: str) -> str:
    """Extract clean text content from HTML, excluding code blocks."""
    if not html.strip():
        return ''
    
    try:
        # The html parameter now contains clean text content from Playwright
        # Just format it with the section header
        if len(html.strip()) > 10:  # Only include if there's substantial content
            return f'## {tab_name}\n\n{html.strip()}\n\n'
        else:
            return f'## {tab_name}\n\n'
    except Exception as e:
        logger.warning(f'Failed to extract text from tab {tab_name}: {e}')
        return ''
