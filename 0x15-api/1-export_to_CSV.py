#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import requests
import sys


if __name__ == '__main__':
    employeeId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employeeId

    response = requests.get(url)
    employeeName = response.json().get('name')

    todoUrl = url + "/todos"
    tresponse = requests.get(todoUrl)
    tasks = tresponse.json()
    done = 0
    done_tasks = []
    with open('{}.csv'.format(employeeId), 'a') as f:
        for task in tasks:
            f.write('"{}","{}","{}","{}\n'.format(
                employeeId, response.json().get('username'),
                task.get('completed'),
                task.get('title')))
