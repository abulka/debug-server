import requests
import random
from lib.fancy_panel import example_table_json_string
from lib.fancy_panel_tree import example_json_data
import json


BASE_URL = 'http://localhost:5050'

def hello_world():
    url = f'{BASE_URL}/hello'
    response = requests.get(url)
    print(f'Status code: {response.status_code}, Reason: {response.reason}')
    # print(f'Raw response content: {response.content}')
    # print(f'Hello world response: {response.text}')

def log_message(filename, content):
    url = f'{BASE_URL}/log'
    data = {
        'filename': filename,
        'content': content
    }
    response = requests.post(url, json=data)
    print(f'Status code: {response.status_code}, Reason: {response.reason}')
    print(f'Raw response content: {response.content.decode("utf-8")}')
    try:
        print(f'Log response: {response.json()}')
    except requests.exceptions.JSONDecodeError:
        print('Failed to decode JSON response')

def get_files():
    url = f'{BASE_URL}/files'
    response = requests.get(url)
    print(f'Status code: {response.status_code}, Reason: {response.reason}')
    print(f'Raw response content: {response.content.decode("utf-8")}')
    try:
        print(f'Files response: {response.json()}')
    except requests.exceptions.JSONDecodeError:
        print('Failed to decode JSON response')

def get_file_content(filename):
    url = f'{BASE_URL}/files/{filename}'
    response = requests.get(url)
    print(f'Status code: {response.status_code}, Reason: {response.reason}')
    print(f'Raw response content: {response.content.decode("utf-8")}')
    try:
        print(f'File content response: {response.json()}')
    except requests.exceptions.JSONDecodeError:
        print('Failed to decode JSON response')

def sync():
    url = f'{BASE_URL}/sync'
    data = {
        'content': 'hello'
    }
    response = requests.post(url, json=data)
    print(f'Status code: {response.status_code}, Reason: {response.reason}')
    print(f'Raw response content: {response.content.decode("utf-8")}')
    try:
        print(f'Sync response: {response.json()}')
    except requests.exceptions.JSONDecodeError:
        print('Failed to decode JSON response')

def big_message():
    msg = ""
    for i in range(100):
        random_number = random.randint(1, 100)
        msg += f"<p>this is line {i} random {random_number}</p>"
    log_message('long.txt', msg)

def clear_logs():
    url = f'{BASE_URL}/clear'
    response = requests.delete(url)
    print(f'Status code: {response.status_code}, Reason: {response.reason}')
    print(f'Raw response content: {response.content.decode("utf-8")}')
    try:
        print(f'Clear logs response: {response.json()}')
    except requests.exceptions.JSONDecodeError:
        print('Failed to decode JSON response')

def clear_log(filename):
    url = f'{BASE_URL}/clear/{filename}'
    response = requests.delete(url)
    print(f'Status code: {response.status_code}, Reason: {response.reason}')
    print(f'Raw response content: {response.content.decode("utf-8")}')
    try:
        print(f'Clear log response: {response.json()}')
    except requests.exceptions.JSONDecodeError:
        print('Failed to decode JSON response')

def demo1():
    # clear_logs()

    # Get hello world
    hello_world()
    # exit(0)

    # Log a message
    log_message('test.log', 'This is a test log message.')
    log_message('hello.log', '<p>Invidunt dolor lorem elitr takimata at stet est no gubergren eos, stet eirmod sed no elitr aliquyam aliquyam eos et..</p>')

    # Get list of files
    get_files()

    # Get content of a specific file
    # get_file_content('test.log')

    # Call /sync endpoint
    # sync()

    big_message()


def demo2():

    # Clear the specific log file
    clear_log(filename='my_fancy_panel.json')

    # Convert example_table_json_string to a dict
    data = json.loads(example_table_json_string)

    # Modify population levels randomly
    for dict in data:
        if 'population' in dict:
            dict['population'] = random.randint(1000, 1000000)

    # Convert back to json
    modified_json_string = json.dumps(data, indent=4)
    # print(modified_json_string)
    log_message('my_fancy_panel.json', modified_json_string)

if __name__ == '__main__':

    # demo1()
    demo2()