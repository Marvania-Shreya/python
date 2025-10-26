"""
 Challenge: Terminal-Based Task List Manager

Create a Python script that lets users manage a to-do list directly from the terminal.

Your program should:
1. Allow users to:
   - Add a task
   - View all tasks
   - Mark a task as completed
   - Delete a task
   - Exit the app
2. Save all tasks in a text file named `tasks.txt` so data persists between runs.
3. Display tasks with an index number and a ✔ if completed.

Example menu:
1. Add Task  
2. View Tasks  
3. Mark Task as Completed  
4. Delete Task  
5. Exit

Example output:
Your Tasks:

Buy groceries||not_done
Finish Python project||done
Read a || book||not_done


Bonus:
- Prevent empty tasks from being added
- Validate task numbers before completing/deleting
"""

import os   # lets us check if file exists

TASK_FILE = "tasks.txt"   # file where we will store all tasks


# -------------------- LOAD TASKS --------------------
def load_tasks():
    tasks = []   # start with an empty list
    if(os.path.exists(TASK_FILE)):   # check if file already exists
        with open(TASK_FILE, 'r', encoding="utf-8") as f:   # open file in read mode
            for line in f:   # go through each line in the file
                text, status = line.strip().rsplit("||", 1)  # split into task text and status
                tasks.append({"text": text, "done": status == "done"})  
                # store as dictionary {"text": "task name", "done": True/False}
    return tasks   # return the list of tasks


# -------------------- SAVE TASKS --------------------
def save_tasks(tasks):
    with open(TASK_FILE, "w", encoding="utf-8") as f:   # open file in write mode (overwrite)
        for task in tasks:   # go through each task
            status = "done" if task["done"] else "not_done"   # check task status
            f.write(f"{task['text']}||{status}\n")   # write into file as "text||done/not_done"


# -------------------- DISPLAY TASKS --------------------
def display_tasks(tasks):
    if not tasks:   # if no tasks in the list
        print(f"NO tasks found")
    else:
        for i, task in enumerate(tasks, 1):   # number tasks starting from 1
            checkbox = "✅" if task["done"] else " "   # show tick if done
            print(f"{i}. [{checkbox}] {task['text']}")   # print task with number
    print()   # just print a blank line for spacing


# -------------------- MAIN PROGRAM --------------------
def task_manager():
    tasks = load_tasks()   # load all tasks at start

    while True:   # loop forever until user exits
        # print menu
        print("\n------Task List Manager -------")
        print("1. Add task")
        print("2. View Tasks")
        print("3. Mark Task as complete")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()   # ask user for choice

        match choice:   # check which option user selected
            # ----------------- Add Task -----------------
            case "1":
                text = input("Enter your task: ").strip()   # ask for task text
                if text:   # if not empty
                    tasks.append({"text":text, "done": False})   # add new task as not done
                    save_tasks(tasks)   # save updated list to file
                else:
                    print("Task cannot be empty")

            # ----------------- View Tasks -----------------
            case "2":
                display_tasks(tasks)   # show all tasks

            # ----------------- Mark Task Complete -----------------
            case "3":
                display_tasks(tasks)   # show tasks first
                try:
                    num = int(input("Enter task number"))   # ask for task number
                    if 1 <= num <= len(tasks):   # check if valid number
                        tasks[num-1]["done"] = True   # mark that task as done
                        save_tasks(tasks)   # save to file
                        print("task marked as DONE")
                    else:
                        print("Invalid task number")   # if number out of range
                except ValueError:   # if user types not a number
                    print("Please enter a number")

            # ----------------- Delete Task -----------------
            case "4":
                display_tasks(tasks)   # show tasks
                try:
                    num = int(input("Enter task number to delete"))   # ask which task
                    if 1 <= num <= len(tasks):
                        removed = tasks.pop(num-1)   # remove from list
                        save_tasks(tasks)   # save updated list
                        print(f"task removed {removed['text']}")   # show removed task
                    else:
                        print("Invalid task number")
                except ValueError:
                    print("Please enter a number")

            # ----------------- Exit -----------------
            case "5":
                print("Exiting task Manager")
                break   # exit the loop → end program

            # ----------------- Wrong Input -----------------
            case _:
                print("Please choose a valid option")   # handle wrong menu choice


# run the program
task_manager()
