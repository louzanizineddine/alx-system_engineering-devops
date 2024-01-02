#!/usr/bin/python3
"""Exprt data of all employees to json format"""

import requests
from json import dump
from sys import argv

if __name__ == "__main__":
    users_result = requests.get(
        "https://jsonplaceholder.typicode.com/users").json()

    big_dict = {}

    for u in users_result:
        todo_list = []
        td = f"https://jsonplaceholder.typicode.com/users/{u.get('id')}/todos"
        nm_url = f"https://jsonplaceholder.typicode.com/users/{u.get('id')}"

        todo_result = requests.get(td).json()
        name_result = requests.get(nm_url).json()

        for todo in todo_result:
            todo_dict = {
                "username": name_result.get("username"),
                "task": todo.get("title"),
                "completed": todo.get("completed")
            }
            todo_list.append(todo_dict)

        big_dict[u.get("id")] = todo_list

    with open("todo_all_employees.json", 'w') as file:
        dump(big_dict, file)
