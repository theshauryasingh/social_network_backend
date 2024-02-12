import requests
import json
'''
[
    {
        "id": 1,
        "name": "shaurya",
        "username": "theshauryasingh",
        "email": "shaurya@gmail.com",
        "password": "theshauryasingh"
    },
    {
        "id": 2,
        "name": "elon musk",
        "username": "elonmusk",
        "email": "elon@gmail.com",
        "password": "elonmusk"
    },
    {
        "id": 6,
        "name": "mark",
        "username": "mark",
        "email": "markzuckerberg@gmail.com",
        "password": "mark"
    },
    {
        "id": 7,
        "name": "mark",
        "username": "markfake",
        "email": "mark@gmail.com",
        "password": "mark"
    }
]
'''

def signup():
    URL = "http://127.0.0.1:8000/users/signup/"

    data = {
        "name" : "mark zuckerberg",
        "username" : "mark",
        "email" : "markzuckerberg@gmail.com",
        "password" : "mark"
    }
    headers = {'content-Type': 'application/json'}

    json_data = json.dumps(data)
    r = requests.post(url = URL, headers=headers, data = json_data)
    print('.......... ',URL, r)
    data = r.json()
    print(data)

def login():
    URL = "http://127.0.0.1:8000/users/signin/"

    data = {
        "username" : "mark",
        "password" : "mark"
    }
    headers = {'content-Type': 'application/json'}

    json_data = json.dumps(data)
    r = requests.post(url = URL, headers=headers, data = json_data)
    print('.......... ',URL, r)
    data = r.json()
    print(data)

def list_users():
    URL = "http://127.0.0.1:8000/users/"
    headers = {'content-Type': 'application/json', "Authorization": "Token 71cb9fad0d7d0c6d42d35f1937db4b9574d91c59"}
    r = requests.get(url = URL, headers=headers)
    print(URL, r)
    data = r.json()
    print(data)

def list_user(id):
    URL = f"http://127.0.0.1:8000/users/{id}/"
    headers = {'content-Type': 'application/json', "Authorization": "Token 71cb9fad0d7d0c6d42d35f1937db4b9574d91c59"}
    r = requests.get(url = URL, headers=headers)
    print(URL, r)
    data = r.json()
    print(data)

def update_user(id):
    URL = f"http://127.0.0.1:8000/users/{id}/"

    data = {
        'name' : "shaurya singh",
        'username' : "theshauryasingh"
    }
    headers = {'content-Type': 'application/json', "Authorization": "Token 7a4316b4be7a1295e9401ef1a439cbff80c5f8e0"}
    json_data = json.dumps(data)
    r = requests.patch(url = URL, headers=headers, data = json_data)
    print(URL, r)
    data = r.json()
    print(data)

def delete_user(id):
    URL = f"http://127.0.0.1:8000/users/{id}/"

    data = {
        'username' : "mark"
    }
    headers = {'content-Type': 'application/json', "Authorization": "Token 7a4316b4be7a1295e9401ef1a439cbff80c5f8e0"}
    json_data = json.dumps(data)
    r = requests.delete(url = URL, headers=headers, data = json_data)
    print(URL, r)

def update_friend_request_status(request_id, new_status, token):
    url = f"http://127.0.0.1:8000/friend-requests/updatestatus"
    headers = {'content-Type': 'application/json'} #, 'Authorization': f'Token {token}'}
    data = {'status': new_status, 'pk': request_id}

    response = requests.patch(url=url, headers=headers, json=data)

    if response.status_code == 200:
        print("Friend request status updated successfully")
    else:
        print(f"Failed to update friend request status. Status code: {response.status_code}")
        print(response.json())


def create_friend_request(sender_id, receiver_id):
    url = f"{BASE_URL}/friend-requests/"
    data = {
        "fromuser": sender_id,
        "touser": receiver_id
    }
    response = requests.post(url, headers=headers, json=data)
    print("Create Friend Request:", response.json())


def list_friends():
    url = f"{BASE_URL}/friend-requests/"
    params = {'status': "accepted"}
    response = requests.get(url, headers=headers, params=params)
    print('list_friends ', response.json())

# Method to list pending friend requests
def list_pending_friend_requests():
    url = f"{BASE_URL}/friend-requests/"
    params = {'status': "pending"}
    response = requests.get(url, headers=headers, params=params)
    print('list_pending_friend_requests ', response.json())
# signup()
# login()
# list_users()
# update_user(1)
# delete_user(2)
# list_user(1)
# get_friends()
# get_pending_req()


BASE_URL = "http://127.0.0.1:8000"

# Token for authentication
TOKEN = "2d38df850651981d2342d5abb803e3d97751075e"

# Headers with authentication token
headers = {
    "Authorization": f"Token {TOKEN}",
    "Content-Type": "application/json"
}

sender_id = 1
receiver_id = 2
request_id = 1

# create_friend_request(sender_id, receiver_id)

# list_friends()

update_friend_request_status(1, "accepted", TOKEN)

# list_pending_friend_requests()