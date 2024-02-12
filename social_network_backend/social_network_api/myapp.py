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

# ===============================================================================================
# ===============================================================================================

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

def list_users(headers):
    URL = "http://127.0.0.1:8000/users/"
    r = requests.get(url = URL, headers=headers)
    print(URL, r)
    data = r.json()
    print(data)

def list_user(id, headers):
    URL = f"http://127.0.0.1:8000/users/{id}/"
    r = requests.get(url = URL, headers=headers)
    print(URL, r)
    data = r.json()
    print(data)

def update_user(id, headers):
    URL = f"http://127.0.0.1:8000/users/{id}/"

    data = {
        'name' : "shaurya singh",
        'username' : "theshauryasingh"
    }
    json_data = json.dumps(data)
    r = requests.patch(url = URL, headers=headers, data = json_data)
    print(URL, r)
    data = r.json()
    print(data)

def delete_user(id, headers):
    URL = f"http://127.0.0.1:8000/users/{id}/"

    data = {
        'username' : "mark"
    }
    json_data = json.dumps(data)
    r = requests.delete(url = URL, headers=headers, data = json_data)
    print(URL, r)

# ===============================================================================================
# ===============================================================================================

def update_friend_request_status(request_id, new_status, headers):
    url = f"http://127.0.0.1:8000/friendrequests/updatestatus/"
    data = {'status': new_status, 'id': request_id}
    response = requests.patch(url=url, headers=headers, json=data)

    if response.status_code == 200:
        print("Friend request status updated successfully")
    else:
        print(f"Failed to update friend request status. Status code: {response.status_code}")
        print(response.json())


def create_friend_request(sender_id, receiver_id, headers):
    url = f"{BASE_URL}/friendrequests/"
    data = {
        "fromuser": sender_id,
        "touser": receiver_id
    }
    response = requests.post(url, headers=headers, json=data)
    print("Create Friend Request:", response.json())

def list_friends(headers):
    url = f"{BASE_URL}/friendrequests/"
    params = {'status': "accepted"}
    response = requests.get(url, headers=headers, params=params)
    print('list_friends ', response.json())

# Method to list pending friend requests
def list_pending_friend_requests(headers):
    url = f"{BASE_URL}/friendrequests/"
    params = {'status': "pending"}
    response = requests.get(url, headers=headers, params=params)
    print('list_pending_friend_requests ', response.json())

def search_users(query, headers):
    url = f"{BASE_URL}/users/searchusers/"
    params = {'q': query}
    response = requests.get(url, headers=headers, params=params)
    print('search_users ', response.json())

# ===============================================================================================
# ===============================================================================================

BASE_URL = "http://127.0.0.1:8000"
TOKEN = "2d38df850651981d2342d5abb803e3d97751075e"

headers = {
    "Authorization": f"Token {TOKEN}",
    "Content-Type": "application/json"
}

sender_id = 1
receiver_id = 2
request_id = 1

# signup()
# login()
# list_users(headers)
# update_user(1, headers)
# delete_user(2, headers)
# list_user(1, headers)

# create_friend_request(sender_id, receiver_id, headers)
# list_friends(headers)
# update_friend_request_status(1, "accepted", headers)
# list_pending_friend_requests(headers)

search_users('ma', headers)