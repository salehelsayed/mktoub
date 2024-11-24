"""Configuration settings for the application."""
import os

# Base directory of the application
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Documentation directory
DOCS_DIR = os.path.join(BASE_DIR, 'docs-www')

# Markdown extensions
MARKDOWN_EXTENSIONS = [
    'fenced_code',
    'tables',
    'toc',
    'nl2br',
    'sane_lists',
    'attr_list',
    'def_list',
    'mdx_truly_sane_lists'
]

# File patterns
MARKDOWN_PATTERN = '.md'
IGNORED_PATTERNS = ['.git', '__pycache__', '.env']

# Server settings
DEBUG = True
HOST = '0.0.0.0'
PORT = 5000
