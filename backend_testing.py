import requests
from flask import request


def post(name):
    response = requests.post("http://127.0.0.1:5000/users/11", json={'user_name': name})
    print(response)


def test() -> bool:
    user_name = input('Enter a user name')
    try:
        post(user_name)
        if










