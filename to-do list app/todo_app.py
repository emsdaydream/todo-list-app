# todo_app.py
from app.todo import Todo

def main():
    todo = Todo()

    while True:
        print("\n=== To-Do List App ===")
        print(todo)

        print("\nOptions:")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. Delete Task")
        print("0. Exit")

        choice = input("Enter your choice (0-3): ")

        if choice == "0":
            print("Exiting the To-Do List App. Goodbye!")
            break
        elif choice == "1":
            description = input("Enter task description: ")
            todo.add_task(description)
        elif choice == "2":
            index = int(input("Enter task description: "))
            todo.mark_task_completed(index)
        elif choice == "3":
            index = int(input("Enter task number to delete: ")) - 1
            todo.delete_task(index)
        else:
            print("Invalid choice. Please enter a number between 0 and 3")


if __name__ == "__main__":
    main()