"""Utility functions for the application."""
import os
import re
from typing import List, Dict, Any
import markdown
from config import DOCS_DIR, MARKDOWN_EXTENSIONS, IGNORED_PATTERNS, MARKDOWN_PATTERN

class MarkdownProcessor:
    def __init__(self):
        self.md = markdown.Markdown(extensions=MARKDOWN_EXTENSIONS)
        
    def process_content(self, content: str, file_path: str) -> str:
        """Process markdown content and handle internal links."""
        try:
            # Convert markdown to HTML
            html = self.md.convert(content)
            
            # Process internal links
            html = self._process_internal_links(html, file_path)
            
            return html
        except Exception as e:
            raise ProcessingError(f"Error processing markdown: {str(e)}")
            
    def _process_internal_links(self, html: str, file_path: str) -> str:
        """Process internal links in the markdown content."""
        def replace_link(match):
            link_text = match.group(1)
            link_path = match.group(2)
            
            if link_path.startswith(('http://', 'https://', '/')):
                return match.group(0)
                
            try:
                current_dir = os.path.dirname(file_path)
                resolved_path = os.path.normpath(os.path.join(current_dir, link_path))
                relative_path = os.path.relpath(resolved_path, DOCS_DIR).replace('\\', '/')
                
                return f'<a href="#" onclick="loadContent(\'{relative_path}\')">{link_text}</a>'
            except Exception as e:
                print(f"Error processing link {link_path}: {e}")
                return match.group(0)
        
        pattern = r'\[([^\]]+)\]\(([^)]+)\)'
        return re.sub(pattern, replace_link, html)

class FileSystemManager:
    @staticmethod
    def get_files_and_dirs(path: str) -> List[Dict[str, Any]]:
        """Get hierarchical structure of files and directories."""
        items = []
        try:
            for item in sorted(os.listdir(path)):
                if any(pattern in item for pattern in IGNORED_PATTERNS):
                    continue
                    
                full_path = os.path.join(path, item)
                is_dir = os.path.isdir(full_path)
                rel_path = os.path.relpath(full_path, DOCS_DIR)
                
                if is_dir:
                    children = FileSystemManager.get_files_and_dirs(full_path)
                    items.append({
                        'name': item,
                        'path': rel_path.replace('\\', '/'),
                        'is_dir': True,
                        'children': children
                    })
                else:
                    if item.endswith(MARKDOWN_PATTERN):
                        items.append({
                            'name': item,
                            'path': rel_path.replace('\\', '/'),
                            'is_dir': False,
                            'children': []
                        })
            
            return sorted(items, key=lambda x: (not x['is_dir'], x['name'].lower()))
        except Exception as e:
            raise FileSystemError(f"Error accessing directory {path}: {str(e)}")

class ProcessingError(Exception):
    """Exception raised for errors in markdown processing."""
    pass

class FileSystemError(Exception):
    """Exception raised for errors in file system operations."""
    pass
