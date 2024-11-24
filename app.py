"""Main application module."""
from flask import Flask, render_template, jsonify
from utils import MarkdownProcessor, FileSystemManager, ProcessingError, FileSystemError
from config import DOCS_DIR, DEBUG, HOST, PORT
import os

app = Flask(__name__)
markdown_processor = MarkdownProcessor()

@app.route('/')
def index():
    """Render the main page with file tree."""
    try:
        files = FileSystemManager.get_files_and_dirs(DOCS_DIR)
        return render_template('index.html', files=files)
    except FileSystemError as e:
        return render_template('error.html', error=str(e)), 500

@app.route('/content/<path:file_path>')
def get_content(file_path):
    """Get the content of a file."""
    try:
        full_path = os.path.join(DOCS_DIR, file_path)
        if not os.path.isfile(full_path):
            return jsonify({'error': 'File not found'}), 404
            
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if file_path.endswith('.md'):
            content = markdown_processor.process_content(content, file_path)
            
        return content
    except FileSystemError as e:
        return jsonify({'error': f"File system error: {str(e)}"}), 500
    except ProcessingError as e:
        return jsonify({'error': f"Processing error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({'error': f"Unexpected error: {str(e)}"}), 500

@app.errorhandler(404)
def not_found_error(error):
    """Handle 404 errors."""
    return jsonify({'error': 'Resource not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=DEBUG, host=HOST, port=PORT)
