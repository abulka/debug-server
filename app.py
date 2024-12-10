import logging
from flask import Flask, request, jsonify
import os
import tempfile
from typing import Any, Dict
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

logging.getLogger('flask_cors').level = logging.DEBUG

# Create a specific directory for logs in the /tmp directory
LOG_DIR = os.path.join(tempfile.gettempdir(), 'debug-server-files')
os.makedirs(LOG_DIR, exist_ok=True)

@app.route("/hello")
def helloWorld():
  return "Hello, cross-origin-world!"

@app.route('/log', methods=['POST'])
def log():
    data: Dict[str, Any] = request.get_json()
    filename = data.get('filename', 'default.log')
    content = data.get('content', '')

    filepath = os.path.join(LOG_DIR, filename)
    with open(filepath, 'a') as f:
        f.write(content + '\n')

    return jsonify({'message': 'Log message written successfully'})

@app.route('/files', methods=['GET'])
def get_list_files():
    files = os.listdir(LOG_DIR)
    return jsonify(files)

@app.route('/clear', methods=['DELETE'])
def clear():
    for file in os.listdir(LOG_DIR):
        os.remove(os.path.join(LOG_DIR, file))
    return jsonify({'message': 'All logs cleared'})

@app.route('/files/<filename>', methods=['GET'])
def get_file(filename):
    filepath = os.path.join(LOG_DIR, filename)
    with open(filepath, 'r') as f:
        content = f.read()
    return jsonify({'filename': filename, 'content': content})

@app.route('/', methods=['GET'])
def view_files_as_html():
    files = os.listdir(LOG_DIR)
    html_content = "<html><body>"
    html_content += "<h1>Log Files</h1>"
    for filename in files:
        filepath = os.path.join(LOG_DIR, filename)
        with open(filepath, 'r') as f:
            content = f.read()
        html_content += f"<h2>{filename}</h2><pre>{content}</pre><hr>"
    html_content += "</body></html>"
    return html_content

if __name__ == '__main__':
    app.run(debug=True, port=5050)
