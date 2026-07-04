from datetime import date
from random import choice
tasks = []
def save_tasks():
    file = open("tasks.txt","w")
    for task in tasks:
        file.write(
                   task["name"]+","+
                   task["priority"]+","+
                   task["date"]+","+
                   task["time"]+","+
                   task["duration"]+","+
                   str(task["completed"])+"\n"
        )
    file.close()
def load_tasks():
    try:
        file = open("tasks.txt", "r")

        for line in file:
            if line.strip() == "":
                continue

            name, priority, date, time, duration, completed = line.strip().split(",")

            tasks.append({
                "name": name,
                "priority": priority,
                "date": date,
                "time": time,
                "duration": duration,
                "completed": completed == "True"
            })

        file.close()

    except FileNotFoundError:
        pass

load_tasks()
def view_tasks():
        if len(tasks) == 0:
            print("no task found")
        else:
            print("\nyour tasks:")
            for i, task in enumerate(tasks,start=1):
                status="completed" if task["completed"] else "pending"
                print(f"{i}.{task['name']}|priority:{task['priority']}|date:{task['date']}|time:{task['time']}|duration:{task['duration']}|{status}")
view_tasks()
def add_task():
    task = input("enter a new task:")
    priority=(input("enter priority (high/medium/low):"))
    date=(input("enter due date (DD/MM/YYYY):"))
    time=(input("enter due time (HH:MM AM/PM):"))
    duration=(input("enter duration (e.g.,2 hours or 30 minutes):"))
    tasks.append({"name": task,"priority":priority,"date":date,"time":time, "duration":duration, "completed": False})
    print("task added successfully:")
def remove_task():
    task_number = int(input("enter a task number to remove:"))
    if 1 <= task_number <= len(tasks):
         tasks.pop(task_number - 1)
         print("task removed successfully!")
    else:
         print("invalid task number! please try again.")
def mark_completed():
     task_number=int(input("enter task number to mark as completed:"))
     if 1 <= task_number <= len(tasks):
         tasks[task_number-1]["completed"] = True
         print("task marked as successfully!")
     else:
         print("invalid task number! please try again.")
def exit_app():
     save_tasks()
     print("Thank you for using TO DO App!")
def delete_all_task():
    confirm = input("are you sure  you want to delete all tasks? (yes/no):")
    if confirm.lower() == "yes":
     tasks.clear()
     print("all tasks deleted successfully!")
    else:
        print("deletion cancelled.")
def edit_task():
    task_number = int(input("enter task number to edit:"))
    if 1 <= task_number <= len(tasks):
        new_task = input("enter a new task name:")
        new_priority =(input("enter priority (high/medium/low):"))
        tasks[task_number-1]["name"] = new_task
        tasks[task_number-1]["priority"] = new_priority
        print("task updated successfully!")
    else:
        print("invalid task number! please try again.")
def total_tasks():
     total=len(tasks)
     print("total tasks:",total)
def completed_task():
    for task in tasks:
        if task["completed"]==True:
          print(task["name"])
def search_task():
    search=input("enter task name to search:")
    found=False
    for task in tasks:
        if search.lower() in task["name"].lower():
            status="completed" if task["completed"] else "pending"
            print(f"{task['name']}|priority:{task['priority']}|{status}")
            found=True
    if not found:
        print("task not found!")
def pending_task():
    for task in tasks:
        if not task["completed"]:
            status="pending"
            print(f"{task['name']}|priority:{task['priority']}|{status}")
def today_tasks():
    today=input("enter today's date(DD/MM/YYYY):")
    for task in tasks:
        if task["date"]==today:
            status="completed" if task["completed"] else "pending"
            print(f"{task['name']}|priority:{task['priority']}|time:{task['time']}|{status}")

while True:
 print( "=====TO-DO LIST=====")
 print("1. View Task")
 print("2. Add Task")
 print("3. Remove Task")
 print("4. mark task as completed")
 print("5. Exit")
 print("6. delete all tasks")
 print("7. edit task")
 print("8. show total tasks")
 print("9. show completed tasks")
 print("10.search task")
 print("11.show pending tasks")
 print("12.show today's tasks")
 choice=input("choose an option:")
 if choice == "1":
     view_tasks()
 elif choice == "2":
     add_task()
 elif choice == "3":
     remove_task()
 elif choice == "4":
     mark_completed()
 elif choice == "5":
     exit_app()
     break
 elif choice == "6":
     delete_all_task()
 elif choice == "7":
      edit_task()
 elif choice == "8":
      total_tasks()
 elif choice == "9":
      completed_task()
 elif choice == "10":
      search_task()
 elif choice == "11":
      pending_task()
 elif choice == "12":
      today_tasks()
 else:
     print("invalid option1 please try again.")
