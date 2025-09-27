#!/usr/bin/env python3
"""
Concatenate Splunk UI Kit documentation into a logical structure for agent coding.
Organizes docs by category and importance for development reference.
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Tuple

def parse_frontmatter(content: str) -> Tuple[Dict, str]:
    """Extract frontmatter and content from markdown file."""
    if not content.startswith('---'):
        return {}, content
    
    parts = content.split('---', 2)
    if len(parts) < 3:
        return {}, content
    
    frontmatter = {}
    for line in parts[1].strip().split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            frontmatter[key.strip()] = value.strip().strip("'\"")
    
    return frontmatter, parts[2].strip()

def categorize_docs(docs_dir: Path) -> Dict[str, List[Tuple[str, str, Dict]]]:
    """Categorize documentation files by type and importance."""
    categories = {
        'overview': [],
        'react_components': [],
        'accessibility': [],
        'themes_styling': [],
        'visualizations': [],
        'utilities': [],
        'build_tools': [],
        'other_packages': []
    }
    
    for file_path in docs_dir.glob('*.md'):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        frontmatter, body = parse_frontmatter(content)
        filename = file_path.stem
        
        # Categorize based on filename patterns
        if 'overview' in filename.lower():
            categories['overview'].append((filename, content, frontmatter))
        elif filename.startswith('react-ui-'):
            categories['react_components'].append((filename, content, frontmatter))
        elif filename.startswith('accessibility-'):
            categories['accessibility'].append((filename, content, frontmatter))
        elif filename.startswith('themes-'):
            categories['themes_styling'].append((filename, content, frontmatter))
        elif filename.startswith('visualizations-'):
            categories['visualizations'].append((filename, content, frontmatter))
        elif any(util in filename for util in ['ui-utils', 'time-range-utils', 'search-job', 'splunk-utils']):
            categories['utilities'].append((filename, content, frontmatter))
        elif any(tool in filename for tool in ['create-', 'babel-', 'eslint-', 'stylelint-', 'webpack-']):
            categories['build_tools'].append((filename, content, frontmatter))
        else:
            categories['other_packages'].append((filename, content, frontmatter))
    
    # Sort each category
    for category in categories:
        categories[category].sort(key=lambda x: x[0])
    
    return categories

def generate_concatenated_doc(categories: Dict[str, List[Tuple[str, str, Dict]]], output_path: Path):
    """Generate the concatenated documentation file."""
    
    with open(output_path, 'w', encoding='utf-8') as f:
        # Header
        f.write("""# Splunk UI Kit - Complete Documentation Reference

*Generated from crawled Splunk UI Kit documentation for agent coding assistance*

This document contains comprehensive documentation for the Splunk UI Kit, organized logically for development reference. Each section includes component APIs, examples, and usage patterns.

---

""")

        # Table of Contents
        f.write("## Table of Contents\n\n")
        section_map = {
            'overview': 'Overview & Getting Started',
            'react_components': 'React UI Components',
            'accessibility': 'Accessibility Guidelines',
            'themes_styling': 'Themes & Styling',
            'visualizations': 'Visualizations',
            'utilities': 'Utility Libraries',
            'build_tools': 'Build Tools & Configuration',
            'other_packages': 'Other Packages'
        }
        
        for category, title in section_map.items():
            if categories[category]:
                f.write(f"- [{title}](#{category.replace('_', '-')})\n")
        f.write("\n---\n\n")

        # Generate sections
        for category, title in section_map.items():
            if not categories[category]:
                continue
                
            f.write(f"# {title} {{#{category.replace('_', '-')}}}\n\n")
            
            # Add category description
            descriptions = {
                'overview': 'High-level overviews and getting started guides for the Splunk UI Kit ecosystem.',
                'react_components': 'Individual React UI components with APIs, props, and usage examples.',
                'accessibility': 'Accessibility guidelines and best practices for inclusive design.',
                'themes_styling': 'Theming system, design tokens, and styling utilities.',
                'visualizations': 'Chart and visualization components for data display.',
                'utilities': 'Utility libraries for common functionality like time handling, formatting, etc.',
                'build_tools': 'Build tools, configurations, and development utilities.',
                'other_packages': 'Additional packages and specialized functionality.'
            }
            
            if category in descriptions:
                f.write(f"*{descriptions[category]}*\n\n")
            
            # Add documents in this category
            for filename, content, frontmatter in categories[category]:
                # Extract title from frontmatter or filename
                title = frontmatter.get('title', filename.replace('-', ' ').title())
                package = frontmatter.get('package', '')
                component = frontmatter.get('component', '')
                
                f.write(f"## {title}\n\n")
                
                if package or component:
                    f.write(f"**Package:** `{package}` | **Component:** `{component}`\n\n")
                
                # Add the content (skip frontmatter)
                _, body = parse_frontmatter(content)
                f.write(body)
                f.write("\n\n---\n\n")

def main():
    """Main execution function."""
    docs_dir = Path('../docs')
    output_path = Path('../splunk-ui-kit-complete-docs.md')
    
    if not docs_dir.exists():
        print(f"Error: {docs_dir} directory not found")
        return
    
    print("Categorizing documentation files...")
    categories = categorize_docs(docs_dir)
    
    # Print summary
    total_files = sum(len(files) for files in categories.values())
    print(f"\nFound {total_files} documentation files:")
    for category, files in categories.items():
        if files:
            print(f"  {category}: {len(files)} files")
    
    print(f"\nGenerating concatenated documentation: {output_path}")
    generate_concatenated_doc(categories, output_path)
    
    print(f"✅ Complete! Generated {output_path}")
    print(f"📊 Total size: {output_path.stat().st_size / 1024 / 1024:.1f} MB")

if __name__ == '__main__':
    main()
