#!/usr/bin/python3
"""Returns to-do list data for a given employee ID to JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    uid = argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(uid)
    user = requests.get(url, verify=False).json()
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(uid)
    todo = requests.get(url, verify=False).json()
    name = user.get('username')
    rant = [{"task": rant.get("title"),
          "username": name,
          "completed": rant.get("completed")} for rant in todo]
    jub = {}
    jub[uid] = rant
    with open("{}.json".format(uid), 'w') as filejs:
        json.dump(jub, filejs)
