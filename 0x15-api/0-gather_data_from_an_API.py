#!/usr/bin/python3
""" A python Scripts that uses a REST API for 
a given employee ID and returns information about
his/her ToDO list progress
"""

import json
import requests
import sys

# declaring API endpoints
todo_url = f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}/todos'
usr_url = f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}'

# fetching requests
r_todo = requests.get(todo_url)
r_usr = requests.get(usr_url)

# converting json to dictionary
usr = json.loads(r_usr.text)
todo = json.loads(r_todo.text)

#declaring variables
emp_name = usr['name']
complTask = 0
notComplTask = 0
title = []

# looping through the dictionary
for i in todo:
    if i['completed'] == True:
        complTask += 1
    else:
        notComplTask += 1

    title.append(i['title'])

#output the code
print('Employee {} is done with tasks ({}/{}): '.format(
    emp_name, complTask, (notComplTask + complTask)
))
for i in todo:
    if i['completed'] == True:
        print('     {}'.format(i['title']))
