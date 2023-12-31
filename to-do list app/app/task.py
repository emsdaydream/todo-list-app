# app/task.py
from datetime import datetime, timedelta

class Task:
    def __init__(self, description, due_date=None, category=None, completed=False):
        self.description = description
        self.due_date = due_date
        self.category = category
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def is_due_soon(self, days=1):
        if self.due_date:
            return datetime.now() + timedelta(days=days) >= self.due_date
        return False

    def is_overdue(self):
        if self.due_date:
            return datetime.now() > self.due_date
        return False

    def __str__(self):
        status = "[✔]" if self.completed else "[ ]"
        due_date_str = f" (Due: {self.due_date})" if self.due_date else ""
        category_str = f" (Category: {self.category})" if self.category else ""
        return f"{status} {self.description}{due_date_str}{category_str}"
