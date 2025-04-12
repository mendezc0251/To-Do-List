import os

def display_menu():
    print("\nTo-Do List Menu")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
    choice = input("Enter your choice: ")
    return choice
def add_task(task):
       TDL = open("To-Do-List.txt", "a")
       TDL.write(task + "\n")
       TDL.close()
def view_tasks():
      TDL = open("To-Do-List.txt", "r")
      tasks = TDL.readlines()
      TDL.close()
      print("\nYour To-Do List:")
      for i, task in enumerate(tasks, start=1):
          print(f"{i}. {task.strip()}")
def remove_task(task_number):
        TDL = open("To-Do-List.txt", "r")
        tasks = TDL.readlines()
        TDL.close()
        if 0 < task_number <= len(tasks):
            del tasks[task_number - 1]
            TDL = open("To-Do-List.txt", "w")
            TDL.writelines(tasks)
            TDL.close()
            print("Task removed successfully.")
        else:
            print("Invalid task number.")
def main():
    while True:
        choice = display_menu()
        if choice == "1":
            task = input("Enter the task: ")
            add_task(task)
            print("Task added successfully.")
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            task_number = int(input("Enter the task number to remove: "))
            remove_task(task_number)
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")