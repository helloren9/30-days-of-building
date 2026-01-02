import csv
import os

TASKS_FILE = "tasks.csv"

class Task:
    def __init__(self, task_id, description, completed=False):
        self.id = task_id
        self.description = description
        self.completed = completed

def load_tasks():
    tasks = []

    if not os.path.exists(TASKS_FILE):
        return tasks
    
    with open(TASKS_FILE, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            task_id = int(row[0])
            description = row[1]
            completed = True if row[2] == "True" else False
            tasks.append(Task(task_id, description, completed))

    return tasks

def save_tasks(tasks):
    with open(TASKS_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        for task in tasks:
            writer.writerow([task.id, task.description, task.completed])

def add_task(tasks):
    description = input("Enter task description: ")
    task_id = len(tasks) + 1
    new_task = Task(task_id, description)
    tasks.append(new_task)
    print("Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    
    print("\nYour Tasks:")
    for task in tasks:
        status = "✅ Completed" if task.completed else "⏳ Pending"
        print(f"{task.id}. {task.description} - {status}")
    print()

def complete_task(tasks):
    view_tasks(tasks)
    try:
        task_id = int(input("Enter task number to mark as completed: "))
        for task in tasks:
            if task.id == task.id:
                task.completed = True
                print("Task marked as completed!")
                return
        print("Task not found.")
    except ValueError:
        print("Invalid input.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_id = int(input("Enter task number to delete: "))
        for task in tasks:
            if task.id == task.id:
                tasks.remove(task)

                # Reindex IDs
                for i, t in enumerate(tasks):
                    t.id = i + 1

                print("Task deleted!")
                return
        print("Task not found.")
    except ValueError:
        print("Invalid input.")

def main():
    tasks = load_tasks()

    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
