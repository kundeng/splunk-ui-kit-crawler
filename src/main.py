#!/usr/bin/env python3
"""
Splunk UI Kit Documentation Crawler

Crawls the Splunk UI Kit documentation site (splunkui.splunk.com) and extracts
component documentation into well-formatted Markdown files.
"""

import asyncio
import logging
from pathlib import Path
from datetime import timedelta

from crawlee.crawlers import PlaywrightCrawler, PlaywrightCrawlingContext
from crawlee import ConcurrencySettings

from routes import router
from markdown_exporter import MarkdownExporter

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


async def main() -> None:
    """Main crawler entry point."""
    
    # Initialize the markdown exporter (used only for final stats; streaming happens in handlers)
    docs_dir = Path(__file__).parent.parent / "docs"
    exporter = MarkdownExporter(docs_dir)
    
    # Configure the Playwright crawler
    crawler = PlaywrightCrawler(
        # Let auto-discovery crawl the whole site naturally
        max_requests_per_crawl=500,  # Get everything!
        
        # Back to headless mode for production
        headless=True,
        
        browser_type='chromium',
        
        # Use our custom router for handling different page types
        request_handler=router,
        
        # Add some delay between requests to be respectful
        max_request_retries=3,
        request_handler_timeout=timedelta(seconds=60),
        
        # Small viewport to save memory
        browser_new_context_options={
            "viewport": {"width": 1024, "height": 768}
        },
        
        # ENABLE AUTO-DISCOVERY: Follow links automatically
        # max_requests_per_minute=30,  # Be respectful - wrong parameter
    )
    
    # Single root seed - let auto-discovery find everything
    seed_urls = [
        'https://splunkui.splunk.com/home',
    ]
    
    logger.info(f"Starting crawl with {len(seed_urls)} seed URLs")
    logger.info(f"Output directory: {docs_dir}")
    
    try:
        # Run the crawler
        await crawler.run(seed_urls)
        logger.info(f"Crawl completed successfully!")
        
        # Show export stats (files were exported during crawling)
        stats = exporter.get_stats()
        logger.info(f"Exported {stats['total_files']} markdown files to {stats['output_directory']}")
        
    except Exception as e:
        logger.error(f"Crawl failed with error: {e}")
        raise


if __name__ == '__main__':
    asyncio.run(main())
