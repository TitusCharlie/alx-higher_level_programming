#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status using the requests package.
Displays the body of the response with some information.
"""

import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)

    body_type = type(response.text)
    content = response.text

    print("Body response:")
    print("    - type:", body_type)
    print("    - content:", content)

