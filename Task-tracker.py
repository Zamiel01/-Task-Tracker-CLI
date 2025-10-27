import datetime 
import uuid
import json
from pathlib import Path

print("\n_WELCOME_TO_YOUR_TASK_TRACKER_CLI_")

a = Path('task.json')


if not a.exists():
    data = []
    with open('task.json', mode="x", encoding="utf-8") as f:
        json.dump(data, f, indent=4) 

#adds  a new task to the json file
def add_task():
    print("Add your task by following below instructions: ")
    id =  str(uuid.uuid4())
    description = input("Enter short task description (max 30 words):  ")
    status = input("Enter your task status (e.g todo, in-progress, done):  ")
    CreatedAt = str(datetime.datetime.now())
    UpdatedAt = str(datetime.datetime.now())
    with open('task.json', mode="r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except:
            data = []
    with open('task.json', mode="w", encoding="utf-8") as f:
        data.append({
            "id": id,
            "description" : description,
            "status" : status,
            "CreatedAt" : CreatedAt,
            "UpdatedAt" : UpdatedAt,
            }, )
        json.dump(data, f, indent=4)  
        print(f"Task added successfully (ID: {id})")

#updates the task description 
def update_task(i, d):
    with open("task.json", mode="r", encoding='utf-8') as f:
        data = json.load(f)
    for c in data:
        if c["id"] == i:
            c["description"] = d
            c["UpdatedAt"] = str(datetime.datetime.now())
    with open("task.json", mode="w", encoding='utf-8') as f:
        json.dump(data, f, indent=4)
        print("task updated successfully")

#deletes task when given its id
def delete_task(i):
    with open("task.json", mode="r", encoding='utf-8') as f:
        data = json.load(f)
    for c in data:
        if c["id"] == i:
            data.remove(c)
    with open("task.json", mode="w", encoding='utf-8') as f:
        json.dump(data, f, indent=4)
        print("task deleted successfully")

#updates the task status
def update_status(i, d):
    with open("task.json", mode="r", encoding='utf-8') as f:
        data = json.load(f)
    for c in data:
        if c["id"] == i:
            c["status"] = d
            c["UpdatedAt"] = str(datetime.datetime.now())
    with open("task.json", mode="w", encoding='utf-8') as f:
        json.dump(data, f, indent=5)

#list all task 
def list_task():
    with open("task.json", mode="r", encoding='utf-8') as f:
        data = json.load(f)
    for c in data:
        print('\n')
        print(c)

#listing tasks by status
def list_status(s):
    with open("task.json", mode="r", encoding='utf-8') as f:
        data = json.load(f)
    for c in data:
        if c["status"] == s:
            print(c)


    

#Menu options for user   

print("1.Add task")
print("2.Update task")
print("3.Delete task")
print("4.Update task status")
print("5.Display all task")
print("6.Display task by status")
c = int(input("whats your choice ? : "))

if c == 1:
    add_task()
elif c == 2:
    i = str(input("\nEnter the task id to be updated: "))
    d = str(input("\nEnter the new description: "))
    update_task(i, d)
elif c == 3:
    i = str(input("\nEnter the task id to be deleted: "))
    delete_task(i)
elif c == 4:
      i = str(input("\nEnter the task id to be updated: "))
      d = str(input("\nEnter the new status(todo, in-progress, done): "))
      update_status(i,d)
elif c == 5:
    list_task()
elif c == 6:
    i = str(input("Enter task status you wish to print (todo, in-progress, done): "))
    list_status(i)
    