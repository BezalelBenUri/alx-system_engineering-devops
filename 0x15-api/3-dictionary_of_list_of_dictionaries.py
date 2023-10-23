#!/usr/bin/python3
"""Exports to-do list data of all employees to JSON format."""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            uuss.get("id"): [{
                "task": tos.get("title"),
                "completed": tos.get("completed"),
                "username": uuss.get("username")
            } for tos in requests.get(url + "todos",
                                    params={"userId": uuss.get("id")}).json()]
            for uuss in users}, jsonfile)
