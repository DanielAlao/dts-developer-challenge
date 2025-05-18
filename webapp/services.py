import requests

BASE_URL = 'http://localhost:8000/api/tasks/'
TOKEN_URL = 'http://localhost:8000/api/token/'

# Replace with valid Django user credentials
USERNAME = 'admin'
PASSWORD = 'taskapi'


def get_token():
    response = requests.post(TOKEN_URL, json={
        'username': USERNAME,
        'password': PASSWORD
    })

    if response.status_code == 200:
        return response.json()['access']
    else:
        raise Exception('Could not get token: ' + response.text)


def get_auth_headers():
    token = get_token()
    return {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }


def get_all_tasks():
    headers = get_auth_headers()
    response = requests.get(BASE_URL, headers=headers)
    response.raise_for_status()
    return response.json()


def get_task(task_id):
    headers = get_auth_headers()
    response = requests.get(f'{BASE_URL}{task_id}/', headers=headers)
    response.raise_for_status()
    return response.json()


def create_task(title, description, status, due_date):
    headers = get_auth_headers()
    data = {
        "title": title,
        "description": description,
        "status": status,
        "due_date": due_date,
    }
    response = requests.post(BASE_URL, json=data, headers=headers)
    return response.json()


def update_task(task_id, status):
    headers = get_auth_headers()
    response = requests.patch(
        f'{BASE_URL}{task_id}/', json={'status': status}, headers=headers)
    response.raise_for_status()
    return response.json()


def delete_task(task_id):
    headers = get_auth_headers()
    response = requests.delete(f'{BASE_URL}{task_id}/', headers=headers)
    response.raise_for_status()
    return response.status_code == 204
