#!/usr/bin/python3
""" Script that exports data for all employees in the JSON format """

import json
import requests


API_URL = "https://jsonplaceholder.typicode.com/"

if __name__ == "__main__":

    employees = requests.get('{}users'.format(API_URL)).json()

    todos_list = requests.get("{}todos".format(API_URL)).json()

    json_file = "todo_all_employees.json"

    with open(json_file, "w") as json_file:
        json.dump({employees.get("id"): [{
            "username": employees.get("username"),
            "task": tasks.get("title"),
            "completed": tasks.get("completed"),
        } for tasks in todos_list]
                   for employees in employees}, json_file)
