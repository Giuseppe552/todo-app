import os
import json

FILENAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        json.dump(tasks, f)

def show_tasks(tasks):
    print("\n📋 To-Do List:")
    if not tasks:
        print("  (No tasks)")
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "❌"
        print(f"  {i}. {task['text']} {status}")
    print()

def main():
    tasks = load_tasks()
    
    while True:
        show_tasks(tasks)
        print("Options:")
        print(" 1. Add Task")
        print(" 2. Mark Task as Done")
        print(" 3. Delete Task")
        print(" 4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            text = input("Enter new task: ")
            tasks.append({"text": text, "done": False})
        elif choice == "2":
            num = int(input("Task number to mark as done: "))
            if 0 < num <= len(tasks):
                tasks[num - 1]["done"] = True
        elif choice == "3":
            num = int(input("Task number to delete: "))
            if 0 < num <= len(tasks):
                tasks.pop(num - 1)
        elif choice == "4":
            save_tasks(tasks)
            print("👋 Goodbye!")
            break
        else:
            print("Invalid option.\n")

if __name__ == "__main__":
    main()
