#!/usr/bin/python3
"""Exprt data of an employee to csv format"""

import requests
import sys
import csv
from csv import  QUOTE_ALL
def get_employee_info(employee_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    info = response.json()
    return info

def get_employee_tasks(employee_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
    tasks = response.json()
    return tasks

def export_to_csv(employee_id, employee_name, tasks):
    file_name = f"{employee_id}.csv"

    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=QUOTE_ALL)

        for task in tasks:
            writer.writerow([employee_id, employee_name, str(task['completed']), task['title']])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    
    employee_info = get_employee_info(employee_id)
    employee_name = employee_info.get("name")
    
    employee_tasks = get_employee_tasks(employee_id)
    
    if employee_name and employee_tasks:
        export_to_csv(employee_id, employee_name, employee_tasks)
        # print(f"CSV file {employee_id}.csv has been created.")
    else:
        print("Employee information not found or tasks unavailable.")
