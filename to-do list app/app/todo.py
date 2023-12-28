# app/todo.py
from app.task import Task

class Todo:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def __str__(self):
        if not self.tasks:
            return "No tasks yet!"
        
        task_list = "\n".join([f"{i + 1}. {task}" for i, task in enumerate(self.tasks)])
        return f"Tasks:\n{task_list}"