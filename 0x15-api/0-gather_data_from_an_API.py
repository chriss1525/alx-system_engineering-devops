#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" Gather data from an API """

import requests
import sys

if __name__ == "__main__":

    argv = sys.argv
    if len(argv) < 2:
        exit()

    url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    response = requests.get(url)
    json_response = response.json()
    name = json_response.get("name")
    employee_id = json_response.get("id")

    todo_url = "https://jsonplaceholder.typicode.com/todos"
    todo_response = requests.get(todo_url)
    todo_json_response = todo_response.json()
    tasks = []

    for task in todo_json_response:
        if task.get("userId") == employee_id:
            tasks.append(task)

    completed_tasks = 0

    for task in tasks:
        if task.get("completed") is True:
            completed_tasks += 1

    print("Employee {} is done with tasks({}/{}):".format(name,
          completed_tasks, len(tasks)))

    for task in tasks:
        if task.get("completed") is True:
            print("\t {}".format(task.get("title")))
