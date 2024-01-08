#!/usr/bin/python3
"""
Lists 10 commits (from the most recent to oldest) of the repository
specified by the user.
"""

import requests
import sys

if __name__ == "__main__":
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = f'https://api.github.com/repos/{owner_name}/{repository_name}/commits'
    params = {'per_page': 10}

    response = requests.get(url, params=params)

    try:
        commits = response.json()
        for commit in commits:
            sha = commit.get('sha')
            author_name = commit.get('commit', {}).get('author', {}).get('name', 'Unknown')
            print(f'{sha}: {author_name}')
    except ValueError:
        print("Could not retrieve commits.")

