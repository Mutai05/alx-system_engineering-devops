#!/usr/bin/python3
"""Script to retrieve TODO list progress of an employee from a given API"""

import requests
from sys import argv


def fetch_todo_list(employee_id):
    """Fetches TODO list progress of an employee from a given API"""
    url_users = 'https://jsonplaceholder.typicode.com/users'
    url_todos = 'https://jsonplaceholder.typicode.com/todos'

    # Retrieve user information
    response_users = requests.get(url_users, params={'id': employee_id})
    employee_info = response_users.json()
    employee_name = employee_info[0]['name']

    # Retrieve TODO list of the employee
    response_todos = requests.get(url_todos, params={'userId': employee_id})
    todos = response_todos.json()

    # Count completed tasks
    completed_tasks = [todo for todo in todos if todo['completed']]
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(todos)

    # Print the progress
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, num_completed_tasks, total_tasks))
    for todo in completed_tasks:
        print("\t {}".format(todo['title']))


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: {} <employee_id>".format(argv[0]))
        exit(1)

    try:
        employee_id = int(argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        exit(1)

    fetch_todo_list(employee_id)
