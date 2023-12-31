# app/todo.py
from .task import Task

class Todo:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date=None, category=None):
        task = Task(description, due_date, category)
        self.tasks.append(task)
        print(f"Added task with category: {category}")  # added

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def get_task_categories(self):
        return set(task.category for task in self.tasks if task.category)

    def __str__(self):
        if not self.tasks:
            return "No tasks in the to-do list."

        task_list = "\n".join(f"{index + 1}. {task}" for index, task in enumerate(self.tasks))
        return f"To-Do List:\n{task_list}"
