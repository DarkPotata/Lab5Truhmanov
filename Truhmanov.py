"""
Simple Todo Manager with tags
"""

class Task:
    def __init__(self, title, description=""):
        self.title = title
        self.description = description
        self.completed = False
        self.tags = []

    def complete(self):
        self.completed = True

    def add_tag(self, tag):
        if tag not in self.tags:
            self.tags.append(tag)

    def remove_tag(self, tag):
        if tag in self.tags:
            self.tags.remove(tag)

    def __str__(self):
        status = "✓" if self.completed else "✗"
        tags_str = f" [{', '.join(self.tags)}]" if self.tags else ""
        return f"[{status}] {self.title}{tags_str}"


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

    def get_tasks_by_tag(self, tag):
        return [t for t in self.tasks if tag in t.tags]

    def get_tag_statistics(self):
        stats = {}
        for task in self.tasks:
            for tag in task.tags:
                stats[tag] = stats.get(tag, 0) + 1
        return stats


def main():
    todo = TodoList()
    todo.add_task("Изучить Git", "Разобраться с ветками и cherry-pick")
    todo.add_task("Сделать лабораторную", "Подготовить репозиторий")
    todo.add_task("Отдохнуть", "Посмотреть сериал")

    task1 = todo.add_task("Почитать документацию", "Прочитать про cherry-pick")
    task1.add_tag("учёба")
    task1.add_tag("git")

    task2 = todo.add_task("Сходить в зал", "Тренировка")
    task2.add_tag("спорт")

    print("Все задачи:")
    for task in todo.get_all_tasks():
        print(f"  {task}")

    print("\nЗадачи с тегом 'учёба':")
    for task in todo.get_tasks_by_tag("учёба"):
        print(f"  {task}")

    print("\nСтатистика по тегам:")
    stats = todo.get_tag_statistics()
    for tag, count in stats.items():
        print(f"  {tag}: {count} задач(а)")

if __name__ == "__main__":
    main()