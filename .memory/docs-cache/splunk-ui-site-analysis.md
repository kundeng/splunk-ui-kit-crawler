---
site: splunk-ui
base_url: https://splunkui.splunk.com/
analysis_date: 2025-09-25T02:43:04-04:00
---

# Splunk UI Site Analysis

## Site Structure
- **Base URL**: https://splunkui.splunk.com/
- **Architecture**: Single Page Application (SPA) with client-side routing
- **Content Rendering**: Fully dynamic via JavaScript bundle (`index.js`)

## Key Sections Discovered
1. **Packages** (`/Packages`) - Main package index with categories:
   - Splunk UI Toolkit (Create, React UI, Dashboard Framework, Visualizations)
   - User Interface (Themes, React Icons, React Page, Toast Notifications, etc.)
   - Utilities (Splunk Utils, UI Utils, SearchJob, Moment)
   - Build Tools (Babel Preset, Webpack Configs)
   - Code Quality (ESLint Config, StyleLint Config)
   - Deprecated packages

2. **Package Details** (e.g., `/Packages/react-ui/Overview`)
   - Overview, Change Log, Licenses, Components, Migration, Testing, Theming
   - Extensive sidebar navigation with component categories (Base, Content, Data Entry, Navigation, Utilities)

3. **Component Pages** (e.g., `/Packages/react-ui/Button`)
   - Rich documentation with examples, usage guidelines, accessibility notes
   - Interactive examples with live components
   - Code blocks with syntax highlighting
   - Tabbed interfaces for different variants
   - Images for design guidelines

## Dynamic Elements & Challenges

### 1. SPA Rendering
- **Challenge**: Server returns only `<div id="main-app-container"></div>` + JS bundle
- **Solution**: Must use Playwright to render JavaScript content
- **Wait Strategy**: `await page.wait_for_selector('main')` or similar content selectors

### 2. Interactive Components
- **Tabs**: Component examples often use tabbed interfaces
- **Accordions**: Collapsible sections for different variants
- **Live Examples**: Interactive React components that demonstrate functionality
- **Code Blocks**: Syntax-highlighted code with copy functionality

### 3. Navigation Structure
- **Primary Nav**: Design System, Toolkits, Packages
- **Secondary Nav**: Package-specific sections (Overview, Components, etc.)
- **Sidebar Nav**: Deep component hierarchy with categories

### 4. Content Types
- **Text Content**: Headings, paragraphs, lists
- **Code Examples**: Multiple code blocks per component
- **Images**: Design guideline illustrations
- **Interactive Examples**: Live component demonstrations

## Crawling Strategy

### URL Patterns
```
https://splunkui.splunk.com/Packages
https://splunkui.splunk.com/Packages/{package-name}/
https://splunkui.splunk.com/Packages/{package-name}/{section}
https://splunkui.splunk.com/Packages/{package-name}/{component}
```

### Key Selectors
- **Main Content**: `main`, `article`
- **Headings**: `h1`, `h2`, `h3`
- **Code Blocks**: `pre code`, `code[class*="language-"]`
- **Navigation Links**: `nav a[href]`
- **Examples**: Interactive component containers

### Link Discovery Strategy
- **Strategy**: `same-domain`
- **Include Patterns**: 
  - `/Packages/**`
  - `/DesignSystem/**` (if needed)
  - `/Toolkits/**` (if needed)
- **Exclude Patterns**: External links, non-doc resources

### Content Extraction
1. **Page Metadata**: Title, URL, breadcrumbs
2. **Main Content**: All text content from main/article
3. **Code Blocks**: Extract with language detection
4. **Images**: Alt text and captions
5. **Navigation Context**: Package name, section, component name

## Implementation Requirements

### Robust Waits
- Wait for main content: `await page.wait_for_selector('main')`
- Wait for navigation: `await page.wait_for_load_state('networkidle')`
- Handle dynamic loading with timeouts

### Content Processing
- Extract and preserve heading hierarchy
- Capture code blocks with language metadata
- Convert to clean Markdown with frontmatter
- Handle image references and alt text

### Rate Limiting
- Conservative crawl speed to respect site
- Random delays between requests
- Proper user agent and headers

### Output Structure
```markdown
---
title: Button Component
package: react-ui
section: Components
url: https://splunkui.splunk.com/Packages/react-ui/Button
crawled_at: 2025-09-25T02:43:04-04:00
type: component
---

# Button Component

[Extracted content with preserved formatting]
```
