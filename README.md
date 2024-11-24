# Documentation Viewer with Mermaid Support

A modern, Flask-based documentation viewer that supports Markdown files and Mermaid diagrams. This application provides an intuitive interface for managing and viewing documentation with a resizable sidebar, hierarchical file navigation, and real-time diagram rendering.

## 🌟 Features

- **Interactive UI**
  - Resizable sidebar with smooth drag functionality
  - Hierarchical file tree navigation
  - Expandable/collapsible folders
  - Modern and clean interface

- **Markdown Support**
  - Full Markdown rendering
  - Code syntax highlighting
  - Table formatting
  - Inline HTML support

- **Mermaid Integration**
  - Real-time diagram rendering
  - Support for flowcharts, sequence diagrams, and more
  - Automatic diagram updates

- **File Management**
  - Easy file navigation
  - Asynchronous file loading
  - Organized file structure
  - Quick access to documentation

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/salehelsayed/mktoub.git
cd mktoub
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Application

1. Start the Flask server:
```bash
python app.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

## 📁 Project Structure

```
mktoub/
├── app.py                 # Flask application entry point
├── templates/            
│   └── index.html        # Main application template
├── static/
│   ├── css/              # Stylesheets
│   └── js/               # JavaScript files
├── docs-www/             # Documentation files
│   ├── Development_Plan/
│   ├── Docu/
│   └── SDLC/
└── requirements.txt      # Python dependencies
```

## 🛠 Technologies Used

- **Backend**
  - Flask (Python web framework)
  - Python 3.8+

- **Frontend**
  - HTML5/CSS3
  - JavaScript (ES6+)
  - Split.js (for resizable layout)
  - Mermaid.js (for diagram rendering)

- **Dependencies**
  - Flask==2.0.1
  - Markdown==3.3.4
  - Python-Markdown-Math==0.8

## 🔧 Configuration

The application can be configured through the following environment variables:

- `FLASK_ENV`: Set to `development` for debug mode
- `PORT`: Server port (default: 5000)
- `HOST`: Server host (default: localhost)

## 📝 Usage

1. **Viewing Documentation**
   - Navigate through folders in the sidebar
   - Click on files to view their content
   - Diagrams are automatically rendered

2. **Adjusting Layout**
   - Drag the sidebar divider to resize
   - Collapse folders for better organization
   - Click on folder arrows to expand/collapse

3. **Working with Mermaid Diagrams**
   - Use \`\`\`mermaid code blocks in markdown
   - Diagrams update automatically
   - Supports multiple diagram types

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Flask](https://flask.palletsprojects.com/) for the web framework
- [Split.js](https://split.js.org/) for the resizable interface
- [Mermaid](https://mermaid-js.github.io/mermaid/#/) for diagram rendering
- [Python-Markdown](https://python-markdown.github.io/) for Markdown processing

## 📞 Contact

Saleh Elsayed - [@salehelsayed](https://github.com/salehelsayed)

Project Link: [https://github.com/salehelsayed/mktoub](https://github.com/salehelsayed/mktoub)
