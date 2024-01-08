#!/usr/bin/python3
"""
Takes GitHub credentials (username and password) and uses the GitHub API to display your id.
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, password))

    try:
        user_data = response.json()
        print(user_data.get('id', 'None'))
    except ValueError:
        print("None")

