# todo_app.py
from app.todo import Todo
from datetime import datetime

def display_notifications(todo):
    print("\n=== Task Notifications ===")
    for task in todo.tasks:
        if task.is_overdue():
            print(f"Overdue: {task}")
        elif task.is_due_soon():
            print(f"Due Soon: {task}")

def main():
    todo = Todo()

    while True:
        print("\n=== To-Do List App ===")
        print(todo)

        print("\nOptions:")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. Delete Task")
        print("4. View Task Categories")
        print("5. View Tasks by Category")
        print("6. View Task Notifications")
        print("0. Exit")

        choice = input("Enter your choice (0-6): ")

        if choice == "0":
            print("Exiting the To-Do List App. Goodbye!")
            break
        elif choice == "1":
            description = input("Enter task description: ")
            expiration_choice = input("Do you want to add an expiration date? (y/n): ").lower()
            if expiration_choice == "y":
                due_date_str = input("Enter due date (optional, format: YYYY-MM-DD HH:MM): ")
                due_date = datetime.strptime(due_date_str, "%Y-%m-%d %H:%M") if due_date_str else None
            elif expiration_choice == "n":
                due_date = None
            else:
                print("Invalid choice for expiration date. Skipping.")
                due_date = None
            category_choice = input("Do you want to add a task category? (y/n): ").lower()
            if category_choice == "y":
                category = input("Enter task category (optional): ")
            elif category_choice == "n":
                category = None
            else:
                print("Invalid choice for task category. Skipping.")
                category = None
            todo.add_task(description, due_date, category)
        elif choice == "2":
            index = int(input("Enter task number to mark as completed: ")) - 1
            todo.mark_task_completed(index)
        elif choice == "3":
            index = int(input("Enter task number to delete: ")) - 1
            todo.delete_task(index)
        elif choice == "4":
            print("\n=== Task Categories ===")
            categories = todo.get_task_categories()
            if categories:
                for category in categories:
                    print(f"- {category}")
            else:
                print("No task categories saved.")
        elif choice == "5":
            selected_category = input("Enter task category to view tasks: ")
            tasks_in_category = [task for task in todo.tasks if task.category == selected_category]
            if tasks_in_category:
                print(f"\n=== Tasks in Category '{selected_category}' ===")
                for task in tasks_in_category:
                    print(f"- {task}")
            else:
                print(f"No tasks found in category '{selected_category}'.")
        elif choice == "6": 
            display_notifications(todo)
        else:
            print("Invalid choice. Please enter a number between 0 and 6.")

if __name__ == "__main__":
    main()
