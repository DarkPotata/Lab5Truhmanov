"""
Simple Todo Manager
"""


class Task:
    def __init__(self, title, description=""):
        self.title = title
        self.description = description
        self.completed = False

    def complete(self):
        self.completed = True

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.title}"


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description=""):
        task = Task(title, description)
        self.tasks.append(task)
        return task

    def get_all_tasks(self):
        return self.tasks

    def get_pending_tasks(self):
        return [t for t in self.tasks if not t.completed]

    def get_completed_tasks(self):
        return [t for t in self.tasks if t.completed]


def main():
    todo = TodoList()
    todo.add_task("Изучить Git", "Разобраться с ветками и cherry-pick")
    todo.add_task("Сделать лабораторную", "Подготовить репозиторий")
    todo.add_task("Отдохнуть", "Посмотреть сериал")

    print("Все задачи:")
    for task in todo.get_all_tasks():
        print(f"  {task}")


if __name__ == "__main__":
    main()