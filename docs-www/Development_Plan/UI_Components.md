# UI Components Documentation

This document provides detailed documentation for the main UI components of our documentation viewer: the Resizable Slider and the File Tree.

## 1. Resizable Slider

The resizable slider allows users to adjust the width of the sidebar by dragging the divider between the sidebar and content area.

### Implementation

#### HTML Structure
```html
<body>
    <div id="sidebar">
        <!-- Sidebar content -->
    </div>
    <div id="content">
        <!-- Main content -->
    </div>
</body>
```

#### CSS
```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    height: 100vh;
    overflow: hidden;
    display: flex;
}

#sidebar {
    width: 250px;
    overflow-y: auto;
    background: #f8f9fa;
    padding: 10px;
}

#content {
    flex-grow: 1;
    overflow-y: auto;
    padding: 20px;
}

.gutter {
    background-color: #eee;
    cursor: col-resize;
    width: 10px;
}
```

#### JavaScript (using Split.js)
```javascript
Split(['#sidebar', '#content'], {
    sizes: [25, 75],
    minSize: [200, 300],
    gutterSize: 10,
    cursor: 'col-resize'
});
```

### Features
- Smooth resizing of sidebar
- Minimum width constraints (200px for sidebar, 300px for content)
- Visual feedback during resizing
- Responsive layout

## 2. File Tree

The file tree component displays folders and files in a hierarchical structure with expandable/collapsible folders.

### Implementation

#### HTML Structure (Jinja2 Template)
```html
{% macro render_tree(items) %}
<ul>
    {% for item in items %}
    <li>
        {% if item.is_dir %}
        <div class="folder-container">
            <span class="folder">{{ item.name }}</span>
            <div class="nested">
                {{ render_tree(item.children) }}
            </div>
        </div>
        {% else %}
        <span class="file" data-path="{{ item.path }}">{{ item.name }}</span>
        {% endif %}
    </li>
    {% endfor %}
</ul>
{% endmacro %}
```

#### CSS
```css
.folder {
    cursor: pointer;
    user-select: none;
    display: block;
    padding: 5px 0;
    position: relative;
}

.folder::before {
    content: "▶";
    margin-right: 5px;
    display: inline-block;
    transform: rotate(0deg);
    transition: transform 0.2s ease;
}

.folder.expanded::before {
    transform: rotate(90deg);
}

.file {
    display: block;
    padding: 5px 0 5px 24px;
    text-decoration: none;
    color: #0066cc;
    cursor: pointer;
}

.file:hover {
    background-color: #e9ecef;
    border-radius: 4px;
}

.file::before {
    content: "📄";
    margin-right: 5px;
}

.nested {
    display: none;
    padding-left: 20px;
}

.nested.active {
    display: block;
}

.folder-container {
    margin: 2px 0;
}

.folder-container:hover {
    background-color: #e9ecef;
    border-radius: 4px;
}
```

#### JavaScript
```javascript
// Add click handlers for folders
document.querySelectorAll('.folder').forEach(folder => {
    folder.addEventListener('click', function() {
        this.classList.toggle('expanded');
        const nested = this.nextElementSibling;
        if (nested && nested.classList.contains('nested')) {
            nested.classList.toggle('active');
        }
    });
});

// Add click handlers for files
document.querySelectorAll('.file').forEach(file => {
    file.addEventListener('click', function(e) {
        e.preventDefault();
        const path = this.getAttribute('data-path');
        loadContent(path);
    });
});

// Function to load file content
async function loadContent(path) {
    try {
        const response = await fetch(`/content/${path}`);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const content = await response.text();
        document.getElementById('markdown-content').innerHTML = content;
        
        // Re-initialize Mermaid after content is loaded
        mermaid.init(undefined, document.querySelectorAll('.mermaid'));
    } catch (error) {
        console.error('Error loading content:', error);
        document.getElementById('markdown-content').innerHTML = 
            `<div class="error">Error loading content: ${error.message}</div>`;
    }
}
```

### Features
- Expandable/collapsible folders with arrow indicators
- Visual feedback on hover
- File icons for better visual hierarchy
- Smooth animations for folder expansion
- Async content loading for files

## Dependencies

1. **Split.js**: Required for the resizable slider functionality
   ```html
   <script src="https://cdnjs.cloudflare.com/ajax/libs/split.js/1.6.5/split.min.js"></script>
   ```

2. **Mermaid.js**: Required for rendering diagrams in markdown content
   ```html
   <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
   ```

## Usage

1. **Resizing the Sidebar**:
   - Hover over the divider between the sidebar and content
   - Click and drag to resize
   - Release to set the new size

2. **Using the File Tree**:
   - Click the arrow (▶) or folder name to expand/collapse folders
   - Click on a file to view its content in the main area
   - Hover over items for visual feedback

## Notes

- The sidebar has a minimum width of 200px and a maximum width of 600px
- Files are loaded asynchronously to prevent UI blocking
- Folders maintain their expanded/collapsed state during the session
- The layout is responsive and adjusts to window resizing
