from flask import Flask, render_template, abort, jsonify
import markdown
import os
from pathlib import Path
import re

app = Flask(__name__)

# Configure markdown extensions with more features
md = markdown.Markdown(extensions=[
    'fenced_code',
    'tables',
    'toc',
    'nl2br',
    'sane_lists',
    'attr_list',
    'def_list',
    'mdx_truly_sane_lists'
])

DOCS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'docs-www')

def get_files_and_dirs(path):
    items = []
    try:
        for item in sorted(os.listdir(path)):
            if item.startswith('.'):
                continue
                
            full_path = os.path.join(path, item)
            is_dir = os.path.isdir(full_path)
            rel_path = os.path.relpath(full_path, DOCS_DIR)
            
            if is_dir:
                children = get_files_and_dirs(full_path)
                items.append({
                    'name': item,
                    'path': rel_path.replace('\\', '/'),
                    'is_dir': True,
                    'children': children
                })
            else:
                if item.endswith('.md'):
                    items.append({
                        'name': item,
                        'path': rel_path.replace('\\', '/'),
                        'is_dir': False,
                        'children': []
                    })
        
        return sorted(items, key=lambda x: (not x['is_dir'], x['name'].lower()))
    except Exception as e:
        print(f"Error in get_files_and_dirs: {e}")
        return []

def process_markdown_content(content, file_path):
    # Convert the markdown to HTML
    html = md.convert(content)
    
    # Process internal links
    def replace_link(match):
        link_text = match.group(1)
        link_path = match.group(2)
        
        if link_path.startswith(('http://', 'https://', '/')):
            return match.group(0)
            
        current_dir = os.path.dirname(file_path)
        resolved_path = os.path.normpath(os.path.join(current_dir, link_path))
        relative_path = os.path.relpath(resolved_path, DOCS_DIR).replace('\\', '/')
        
        return f'<a href="#" onclick="loadContent(\'{relative_path}\')">{link_text}</a>'
    
    pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    html = re.sub(pattern, replace_link, html)
    
    return html

@app.route('/')
def index():
    files = get_files_and_dirs(DOCS_DIR)
    return render_template('index.html', files=files)

@app.route('/content/<path:file_path>')
def get_content(file_path):
    try:
        full_path = os.path.join(DOCS_DIR, file_path)
        if not os.path.isfile(full_path):
            return jsonify({'error': 'File not found'}), 404
            
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if file_path.endswith('.md'):
            content = process_markdown_content(content, file_path)
            
        return content
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
