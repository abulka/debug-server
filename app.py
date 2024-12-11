import logging
from flask import Flask, request, jsonify, render_template_string
import os
import tempfile
from typing import Any, Dict
from flask_cors import CORS
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime
import random

app = Flask(__name__)
CORS(app)

logging.getLogger("flask_cors").level = logging.DEBUG

# Create a specific directory for logs in the /tmp directory
LOG_DIR = os.path.join(tempfile.gettempdir(), "debug-server-files")
os.makedirs(LOG_DIR, exist_ok=True)


class ChangeHandler(FileSystemEventHandler):
    def __init__(self):
        self.modified = False

    def on_modified(self, event):
        self.modified = True


change_handler = ChangeHandler()
observer = Observer()
observer.schedule(change_handler, LOG_DIR, recursive=False)
observer.start()


@app.route("/hello")
def helloWorld():
    return "Hello, cross-origin-world!"


@app.route("/log", methods=["POST"])
def log():
    data: Dict[str, Any] = request.get_json()
    filename = data.get("filename", "default.log")
    content = data.get("content", "")

    filepath = os.path.join(LOG_DIR, filename)
    with open(filepath, "a") as f:
        f.write(content + "\n")

    return jsonify({"message": "Log message written successfully"})


@app.route("/files", methods=["GET"])
def get_list_files():
    files = os.listdir(LOG_DIR)
    return jsonify(files)


@app.route("/clear", methods=["DELETE"])
def clear():
    for file in os.listdir(LOG_DIR):
        os.remove(os.path.join(LOG_DIR, file))
    return jsonify({"message": "All logs cleared"})


@app.route("/files/<filename>", methods=["GET"])
def get_file(filename):
    filepath = os.path.join(LOG_DIR, filename)
    with open(filepath, "r") as f:
        content = f.read()
    return jsonify({"filename": filename, "content": content})


@app.route("/", methods=["GET"])
def view_files_as_html():
    files = os.listdir(LOG_DIR)
    html_content = "<html><body>"
    html_content += "<h1>Log Files</h1>"
    for filename in files:
        filepath = os.path.join(LOG_DIR, filename)
        with open(filepath, "r") as f:
            content = f.read()
        html_content += f"<h2>{filename}</h2><pre>{content}</pre><hr>"
    html_content += """
    <script>
        setInterval(function() {
            fetch('/check_changes')
                .then(response => response.json())
                .then(data => {
                    if (data.modified) {
                        location.reload();
                    }
                });
        }, 2000);
    </script>
    </body></html>
    """
    return html_content


@app.route("/check_changes", methods=["GET"])
def check_changes():
    global change_handler
    modified = change_handler.modified
    change_handler.modified = False
    return jsonify({"modified": modified})


@app.route("/sync", methods=["POST"])
def sync_files():
    data = request.get_json()
    content = data.get("content", "")
    files = os.listdir(LOG_DIR)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    random_word = random.choice(
        [
            "apple",
            "banana",
            "cherry",
            "date",
            "elderberry",
            "fig",
            "grape",
            "honeydew",
            "kiwi",
            "lemon",
            "mango",
            "nectarine",
            "orange",
            "papaya",
            "quince",
            "raspberry",
            "strawberry",
            "tangerine",
            "ugli",
            "vanilla",
            "watermelon",
            "xigua",
            "yellowfruit",
            "zucchini",
            "apricot",
            "blackberry",
            "blueberry",
            "cantaloupe",
            "coconut",
            "cranberry",
            "currant",
            "dragonfruit",
            "durian",
            "gooseberry",
            "grapefruit",
            "guava",
            "jackfruit",
            "kumquat",
            "lime",
            "lychee",
            "mandarin",
            "mulberry",
            "olive",
            "passionfruit",
            "peach",
            "pear",
            "persimmon",
            "pineapple",
            "plum",
            "pomegranate",
            "starfruit",
            "tamarind",
        ]
    )
    for filename in files:
        filepath = os.path.join(LOG_DIR, filename)
        with open(filepath, "a") as f:
            f.write(f"<h3>{current_time} - {random_word} - {content}</h3>\n")
    return jsonify({"message": "Files synchronized successfully"})


if __name__ == "__main__":
    try:
        app.run(debug=True, port=5050)
    finally:
        observer.stop()
        observer.join()
