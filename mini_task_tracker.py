"""
Mini Task Tracker
AI Engineering | Week 1 Assignment

A command-line task management application. Tasks are saved to tasks.json
after every operation and automatically restored when the application starts.
Each task item is stored as a dictionary: {"title": str, "done": bool}
"""

import json

FILE_NAME = "tasks.json"


def load_tasks():
    """Load tasks from tasks.json, or return an empty list if file is missing/empty."""
    tasks = []
    try:
        with open(FILE_NAME, "r") as file:
            tasks = json.load(file)
        print(f"Loaded {len(tasks)} saved task(s) from {FILE_NAME}.")
    except FileNotFoundError:
        print("No saved tasks found. Starting with an empty list.")
    except json.JSONDecodeError:
        print(f"{FILE_NAME} could not be read or is empty. Starting with an empty list.")
    return tasks


def save_tasks(tasks):
    """Save the current task list to tasks.json."""
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    """Prompt the user for a task title and add it as a Pending task."""
    title = input("Task title: ").strip()

    # Input validation: reject blank task names
    if not title:
        print("Task title cannot be empty.")
        return

    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Task added.")


def view_tasks(tasks):
    """Display a numbered list of all tasks along with their status."""
    if not tasks:
        print("No tasks yet.")
        return

    for number, task in enumerate(tasks, start=1):
        status = "Done" if task.get("done") else "Pending"
        print(f"{number}. {task['title']} [{status}]")


def get_task_index(tasks):
    """Prompt for a task number and return the 0-based index, or None if invalid."""
    if not tasks:
        print("No tasks available.")
        return None

    try:
        number = int(input("Task number: "))
    except ValueError:
        print("Invalid input. Please enter a task number.")
        return None

    if number < 1 or number > len(tasks):
        print(f"Invalid task number. Please choose from 1 to {len(tasks)}.")
        return None

    return number - 1


def complete_task(tasks):
    """Mark the selected task as completed."""
    index = get_task_index(tasks)
    if index is None:
        return

    if tasks[index].get("done"):
        print("This task is already completed.")
        return

    tasks[index]["done"] = True
    save_tasks(tasks)
    print("Task completed.")


def delete_task(tasks):
    """Remove the selected task from the list and update storage."""
    index = get_task_index(tasks)
    if index is None:
        return

    removed_task = tasks.pop(index)
    save_tasks(tasks)
    print(f"Task deleted: {removed_task['title']}")


def show_menu():
    """Display the main navigation menu."""
    print("\n--- TASK TRACKER ---")
    print("1. Add  2. View  3. Complete  4. Delete  5. Exit")


def main():
    """Main application loop."""
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Choice: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye! Your tasks are saved in tasks.json.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
