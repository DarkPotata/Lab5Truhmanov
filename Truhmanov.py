"""
Simple Todo Manager with deadlines
"""

from datetime import datetime


class Task:
    def __init__(self, title, description="", deadline=None):
        self.title = title
        self.description = description
        self.completed = False
        self.deadline = deadline  # строка в формате "YYYY-MM-DD"

    def complete(self):
        self.completed = True

    def days_until_deadline(self, current_date):
        if not self.deadline:
            return None
        deadline_date = datetime.strptime(self.deadline, "%Y-%m-%d")
        current = datetime.strptime(current_date, "%Y-%m-%d")
        return (deadline_date - current).days

    def __str__(self):
        status = "✓" if self.completed else "✗"
        deadline_str = f" (до {self.deadline})" if self.deadline else ""
        return f"[{status}] {self.title}{deadline_str}"


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description="", deadline=None):
        task = Task(title, description, deadline)
        self.tasks.append(task)
        return task

    def get_all_tasks(self):
        return self.tasks

    def get_pending_tasks(self):
        return [t for t in self.tasks if not t.completed]

    def get_completed_tasks(self):
        return [t for t in self.tasks if t.completed]

    def get_overdue_tasks(self, current_date):
        overdue = []
        for task in self.tasks:
            if not task.completed and task.deadline and task.deadline < current_date:
                overdue.append(task)
        return overdue


def main():
    todo = TodoList()
    todo.add_task("Изучить Git", "Разобраться с ветками и cherry-pick")
    todo.add_task("Сделать лабораторную", "Подготовить репозиторий")
    todo.add_task("Отдохнуть", "Посмотреть сериал")
    todo.add_task("Сдать отчёт", "Подготовить документы", "2026-04-05")
    todo.add_task("Купить продукты", "Молоко, хлеб", "2026-04-12")

    current = "2026-04-10"

    print("Все задачи:")
    for task in todo.get_all_tasks():
        print(f"  {task}")

    print("\nПросроченные задачи:")
    for task in todo.get_overdue_tasks(current):
        print(f"  {task}")

    task = todo.tasks[3]  # задача с дедлайном "2026-04-05"
    days = task.days_until_deadline(current)
    if days is not None:
        status_word = "дней" if days >= 0 else "просрочено на"
        print(f"\nЗадача '{task.title}': {abs(days)} {status_word}")

if __name__ == "__main__":
    main()