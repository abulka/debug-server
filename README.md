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


# Advanced UI Feature

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
