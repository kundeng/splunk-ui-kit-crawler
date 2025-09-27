#!/usr/bin/env python3
"""
Debug script to understand why BeautifulSoup and HTML-to-Markdown tools 
can't extract code blocks after unhiding them.
"""

import asyncio
import logging
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import html2text
from markdownify import markdownify

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def debug_extraction():
    """Debug the extraction process step by step."""
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # Visible for debugging
        page = await browser.new_page()
        
        try:
            # Navigate to the page
            await page.goto('https://splunkui.splunk.com/Packages/react-ui/CardLayout')
            await page.wait_for_selector('main', timeout=30000)
            await page.wait_for_load_state('networkidle')
            
            # Click on Examples tab
            await page.get_by_role('tab', name='Examples').click()
            await page.wait_for_timeout(1000)
            
            print("=== BEFORE CLICKING SHOW CODE ===")
            
            # Get HTML before clicking
            html_before = await page.content()
            soup_before = BeautifulSoup(html_before, 'html.parser')
            pre_before = soup_before.find_all('pre')
            code_before = soup_before.find_all('code')
            
            print(f"BeautifulSoup BEFORE: {len(pre_before)} pre elements, {len(code_before)} code elements")
            
            # Check with Playwright selectors
            pre_pw_before = await page.query_selector_all('pre')
            code_pw_before = await page.query_selector_all('code')
            print(f"Playwright BEFORE: {len(pre_pw_before)} pre elements, {len(code_pw_before)} code elements")
            
            # Click "Show code" buttons - use simpler selectors
            print("\n=== CLICKING SHOW CODE BUTTONS ===")
            
            # Try to find and click show code buttons
            show_code_buttons = await page.query_selector_all('button:has-text("Show code")')
            print(f"Found {len(show_code_buttons)} Show code buttons")
            
            if len(show_code_buttons) >= 2:
                await show_code_buttons[0].click()
                await page.wait_for_timeout(1000)
                await show_code_buttons[1].click()
                await page.wait_for_timeout(2000)
                print("Clicked both buttons")
            else:
                print("Could not find expected number of buttons")
            
            print("\n=== AFTER CLICKING SHOW CODE ===")
            
            # Get HTML after clicking
            html_after = await page.content()
            soup_after = BeautifulSoup(html_after, 'html.parser')
            pre_after = soup_after.find_all('pre')
            code_after = soup_after.find_all('code')
            
            print(f"BeautifulSoup AFTER: {len(pre_after)} pre elements, {len(code_after)} code elements")
            
            # Check with Playwright selectors
            pre_pw_after = await page.query_selector_all('pre')
            code_pw_after = await page.query_selector_all('code')
            print(f"Playwright AFTER: {len(pre_pw_after)} pre elements, {len(code_pw_after)} code elements")
            
            # If we found pre elements, let's examine them
            if pre_after:
                print(f"\n=== EXAMINING PRE ELEMENTS ===")
                for i, pre in enumerate(pre_after):
                    text = pre.get_text()
                    print(f"PRE {i}: {len(text)} chars, classes: {pre.get('class', [])}")
                    print(f"Preview: {text[:100]}...")
                    
            # Test HTML to Markdown converters
            if pre_after:
                print(f"\n=== TESTING HTML TO MARKDOWN CONVERTERS ===")
                
                # Get just the first pre element's HTML
                first_pre_html = str(pre_after[0])
                
                # Test html2text
                h = html2text.HTML2Text()
                h.ignore_links = False
                h.body_width = 0  # Don't wrap lines
                markdown_html2text = h.handle(first_pre_html)
                print(f"html2text result: {len(markdown_html2text)} chars")
                print(f"Preview: {markdown_html2text[:200]}...")
                
                # Test markdownify
                markdown_markdownify = markdownify(first_pre_html)
                print(f"markdownify result: {len(markdown_markdownify)} chars")
                print(f"Preview: {markdown_markdownify[:200]}...")
                
                # Test on the full main content
                main_element = soup_after.find('main')
                if main_element:
                    main_html = str(main_element)
                    print(f"\n=== TESTING ON FULL MAIN CONTENT ===")
                    print(f"Main HTML: {len(main_html)} chars")
                    
                    # Test html2text on main
                    markdown_main = h.handle(main_html)
                    print(f"html2text on main: {len(markdown_main)} chars")
                    
                    # Save to file for inspection
                    with open('/tmp/debug_main_html.html', 'w') as f:
                        f.write(main_html)
                    with open('/tmp/debug_main_markdown.md', 'w') as f:
                        f.write(markdown_main)
                    print("Saved debug files to /tmp/debug_main_html.html and /tmp/debug_main_markdown.md")
            
            # Keep browser open for manual inspection
            print(f"\n=== BROWSER KEPT OPEN FOR MANUAL INSPECTION ===")
            print("Check the browser window to see the revealed code blocks")
            print("Press Enter to close...")
            input()
            
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(debug_extraction())
