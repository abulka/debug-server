import requests

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
    for i in range(200):
        msg += f"<p>this is line {i}</p>"
    log_message('long.txt', msg)

if __name__ == '__main__':
    # Get hello world
    hello_world()
    # exit(0)

    # Log a message
    log_message('test.log', 'This is a test log message.')
    log_message('hello.log', '<p>Invidunt dolor lorem elitr takimata at stet est no gubergren eos, stet eirmod sed no elitr aliquyam aliquyam eos et..</p>')

    # Get list of files
    get_files()

    # Get content of a specific file
    get_file_content('test.log')

    # Call /sync endpoint
    # sync()

    big_message()
    