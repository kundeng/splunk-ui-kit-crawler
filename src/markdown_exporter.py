"""
Markdown exporter for Splunk UI Kit documentation.

Converts extracted page data into well-formatted Markdown files with frontmatter.
"""

import logging
import re
from pathlib import Path
from typing import Dict, Any, List
from urllib.parse import urlparse
import yaml

logger = logging.getLogger(__name__)


class MarkdownExporter:
    """Exports page data to Markdown files with frontmatter."""
    
    def __init__(self, output_dir: Path):
        """Initialize the exporter with an output directory."""
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        logger.info(f"Markdown exporter initialized with output dir: {self.output_dir}")
    
    def _sanitize_filename(self, text: str) -> str:
        """Convert text to a safe filename."""
        # Remove or replace unsafe characters
        text = re.sub(r'[<>:"/\\|?*]', '-', text)
        # Replace spaces with hyphens
        text = re.sub(r'\s+', '-', text)
        # Remove multiple consecutive hyphens
        text = re.sub(r'-+', '-', text)
        # Remove leading/trailing hyphens
        text = text.strip('-')
        # Ensure it's not empty
        if not text:
            text = 'untitled'
        return text.lower()
    
    def _generate_filename(self, page_data: Dict[str, Any]) -> str:
        """Generate a filename based on page data."""
        page_type = page_data.get('type', 'unknown')
        package = page_data.get('package')
        section = page_data.get('section')
        component = page_data.get('component')
        title = page_data.get('title', 'untitled')
        
        # Build filename based on page type
        if page_type == 'packages_index':
            return 'packages-index.md'
        elif page_type == 'package_overview' and package:
            return f'{self._sanitize_filename(package)}-overview.md'
        elif page_type == 'package_section' and package and section:
            return f'{self._sanitize_filename(package)}-{self._sanitize_filename(section)}.md'
        elif page_type == 'component' and package and component:
            if section:
                return f'{self._sanitize_filename(package)}-{self._sanitize_filename(component)}-{self._sanitize_filename(section)}.md'
            else:
                return f'{self._sanitize_filename(package)}-{self._sanitize_filename(component)}.md'
        else:
            # Fallback to sanitized title
            return f'{self._sanitize_filename(title)}.md'
    
    def _generate_frontmatter(self, page_data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate YAML frontmatter for the page."""
        frontmatter = {
            'title': page_data.get('title', 'Untitled'),
            'url': page_data.get('url'),
            'type': page_data.get('type', 'unknown'),
            'crawled_at': page_data.get('crawled_at'),
        }
        
        # Add optional fields if they exist
        if page_data.get('package'):
            frontmatter['package'] = page_data['package']
        if page_data.get('component'):
            frontmatter['component'] = page_data['component']
        
        # Add tags
        tags = []
        if page_data.get('package'):
            tags.append(page_data['package'])
        if page_data.get('type'):
            tags.append(page_data['type'])
        if tags:
            frontmatter['tags'] = tags
        
        return frontmatter
    
    def _format_content(self, page_data: Dict[str, Any]) -> str:
        """Format the main content as Markdown."""
        content = page_data.get('content', '')
        
        if not content.strip():
            return '<!-- No content extracted -->\n'
        
        # Minimal cleanup: normalize whitespace and preserve original lines.
        # Avoid trying to infer headings, which caused '##' prefixes to appear on code lines.
        lines = [ln.rstrip() for ln in content.split('\n')]
        return '\n'.join(lines) + ('\n' if not content.endswith('\n') else '')
    
    def _format_code_blocks(self, code_blocks: List[Dict[str, Any]]) -> str:
        """Format code blocks as Markdown."""
        if not code_blocks:
            return ''
        
        markdown = '\n## Code Examples\n\n'
        
        for i, block in enumerate(code_blocks):
            language = block.get('language', 'text')
            code = block.get('code', '')
            
            # Normalize line endings and ensure proper whitespace preservation
            if code:
                # Ensure code has proper line endings
                code_lines = code.splitlines()
                # Remove common leading whitespace if present
                if code_lines:
                    # Find minimum indentation (excluding empty lines)
                    non_empty_lines = [line for line in code_lines if line.strip()]
                    if non_empty_lines:
                        min_indent = min(len(line) - len(line.lstrip()) for line in non_empty_lines)
                        # Remove that amount of indentation from all lines
                        code_lines = [line[min_indent:] if line.strip() else line for line in code_lines]
                    
                # Rejoin with consistent line endings
                code = '\n'.join(code_lines)
                
                markdown += f'### Example {i + 1}\n\n'
                markdown += f'```{language}\n{code}\n```\n\n'
        
        return markdown
    
    def _format_props(self, props: List[Dict[str, Any]]) -> str:
        """Format props as a Markdown table if present."""
        if not props:
            return ''

        # Table header
        md = '\n## Props\n\n'
        md += '| Name | Type | Default | Description |\n'
        md += '|------|------|---------|-------------|\n'

        for p in props:
            name = (p.get('name') or '').replace('\n', ' ').strip()
            typ = (p.get('type') or '').replace('\n', ' ').strip()
            default = (p.get('default') or '').replace('\n', ' ').strip()
            desc = (p.get('description') or '').replace('\n', ' ').strip()
            md += f'| {name} | {typ} | {default} | {desc} |\n'

        md += '\n'
        return md
    
    async def export_page(self, page_data: Dict[str, Any]) -> Path:
        """Export a single page to Markdown."""
        try:
            # Generate filename and path
            filename = self._generate_filename(page_data)
            file_path = self.output_dir / filename
            
            # Generate frontmatter
            frontmatter = self._generate_frontmatter(page_data)
            
            # Format content (code blocks are now integrated into content)
            content = self._format_content(page_data)
            
            # Format props
            props_md = self._format_props(page_data.get('props', []))
            
            # Combine into full Markdown document
            markdown_content = '---\n'
            markdown_content += yaml.dump(frontmatter, default_flow_style=False, sort_keys=False)
            markdown_content += '---\n\n'
            markdown_content += content
            if props_md:
                markdown_content += '\n' + props_md
            
            # Write to file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            
            logger.info(f'Exported: {filename}')
            return file_path
            
        except Exception as e:
            logger.error(f'Failed to export page {page_data.get("url", "unknown")}: {e}')
            raise
    
    def get_stats(self) -> Dict[str, Any]:
        """Get export statistics."""
        markdown_files = list(self.output_dir.glob('*.md'))
        return {
            'total_files': len(markdown_files),
            'output_directory': str(self.output_dir),
            'files': [f.name for f in markdown_files]
        }
