# Debug Server

A logging debug server so you can write to multiple log files using an API.

Especially useful for debugging from a browser based application, like vite or react.

## Installation

```bash
uv run app.py
```

## Usage

```python
import requests

json = """
{
    "filename": "mary.txt",
    "content": "hi there the show is on the road"
}
"""
requests.post('http://localhost:5000/log', json=json)
```

All the payloads and results are in JSON format.

# API Endpoints

| Endpoint          | Method | Description                                   |
|--------------------|--------|-----------------------------------------------|
| `/log`            | POST   | Writes a line of text to a specified file.    |
| `/files`          | GET    | Returns a list of files in the temporary directory. |
| `/clear`          | DELETE | Deletes all files in the temporary directory. |
| `/files/{filename}` | GET    | Returns the content of a specific file.      |
| `/sync`           | POST    | Appends a h3 line with the current date time, a random word and the "content" in the payload to all existing files in the LOG_DIR. <br><br>This is useful for marking a certain moment in the app to all log files and thus more easily finding the relevant log messages *after* that point in time. |


# UI Feature

You can view the contents of all the files at once as HTML by visiting the `/` endpoint.

e.g.

```
Log Files

mary.txt
hi there the show is on the road
hi there the show is on the road
hi there the show is on the road
hi there the show is on the road

fred.txt
hi there
hi there
hi there
hi there
hi there
hi there
```

At the moment each file is concatenated after the other in a vertically scrolling HTML page. 

## Future Features

In the future it might be useful to have "windows" for each file that can be scrolled individually.

Custom representations of debug data via plugins could also be useful. Imagine sending up JSON and seeing the result as a table or a graph or a tree or custom HTML object.

# Configuration

There is an auto update feature that will update the UI every 2 seconds.

```bash

# License

MIT

