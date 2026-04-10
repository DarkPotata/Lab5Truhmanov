"""
Simple Todo Manager
"""
import priority


class Task:
    def __init__(self, title, description=""):
        self.title = title
        self.description = description
        self.completed = False
        self.priority = priority  # high, normal, low

    def complete(self):
        self.completed = True

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.title} ({self.priority})"


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description="", priority="normal"):
        task = Task(title, description, priority)
        self.tasks.append(task)
        return task

    def get_all_tasks(self):
        return self.tasks

    def get_pending_tasks(self):
        return [t for t in self.tasks if not t.completed]

    def get_completed_tasks(self):
        return [t for t in self.tasks if t.completed]

    def get_tasks_sorted_by_priority(self):
        priority_order = {"high": 1, "normal": 2, "low": 3}
        return sorted(self.tasks, key=lambda t: priority_order.get(t.priority, 2))

    def get_tasks_by_priority(self, priority):
        return [t for t in self.tasks if t.priority == priority]

def main():
    todo = TodoList()
    todo.add_task("Изучить Git", "Разобраться с ветками и cherry-pick")
    todo.add_task("Сделать лабораторную", "Подготовить репозиторий")
    todo.add_task("Отдохнуть", "Посмотреть сериал")
    todo.add_task("Срочная задача", "Сделать прямо сейчас", "high")
    todo.add_task("Неважная задача", "Можно отложить", "low")

    print("\nЗадачи по приоритету:")
    for task in todo.get_tasks_sorted_by_priority():
        print(f"  {task}")

    print("\nСрочные задачи:")
    for task in todo.get_tasks_by_priority("high"):
        print(f"  {task}")

    print("Все задачи:")
    for task in todo.get_all_tasks():
        print(f"  {task}")


if __name__ == "__main__":
    main()