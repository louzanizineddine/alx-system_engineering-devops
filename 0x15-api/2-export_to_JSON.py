#!/usr/bin/python3
"""Exprt data of an employee to csv format"""

import json
import requests
import sys


def get_employee_info(employee_id):
    response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    info = response.json()
    return info


def get_employee_tasks(employee_id):
    response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
    tasks = response.json()
    return tasks


def export_to_json(employee_id, employee_name, tasks):
    output_data = {employee_id: []}

    for task in tasks:
        task_info = {
            "task": task['title'],
            "completed": task['completed'],
            "username": employee_name
        }
        output_data[employee_id].append(task_info)

    file_name = f"{employee_id}.json"
    with open(file_name, 'w') as file:
        json.dump(output_data, file)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    employee_info = get_employee_info(employee_id)
    employee_name = employee_info.get("username")

    employee_tasks = get_employee_tasks(employee_id)

    if employee_name and employee_tasks:
        export_to_json(employee_id, employee_name, employee_tasks)
        # print(f"JSON file {employee_id}.json has been created.")
    else:
        print("Employee information not found or tasks unavailable.")
