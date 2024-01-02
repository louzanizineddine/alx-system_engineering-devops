#!/usr/bin/python3
"""Use the jsonplacehoder free api to get some data about an employee"""
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


def print_completed_tasks(employee_name, tasks):
    done = [task for task in tasks if task['completed']]
    total = len(tasks)

    print(
        f"Employee {employee_name} is done with tasks({len(done)}/{total}):")
    for task in done:
        print(f"\t {task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    employee_info = get_employee_info(employee_id)
    employee_name = employee_info.get("name")

    employee_tasks = get_employee_tasks(employee_id)

    if employee_name and employee_tasks:
        print_completed_tasks(employee_name, employee_tasks)
    else:
        print("Employee information not found or tasks unavailable.")
