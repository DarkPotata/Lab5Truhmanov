"""
Simple Todo Manager
"""
import priority


class Task:
    def __init__(self, title, description="", deadline=None):
        self.title = title
        self.description = description
        self.completed = False
        self.deadline = deadline  # строка с датой

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

    def get_tasks_sorted_by_priority(self):
        priority_order = {"high": 1, "normal": 2, "low": 3}
        return sorted(self.tasks, key=lambda t: priority_order.get(t.priority, 2))

    def get_tasks_by_priority(self, priority):
        return [t for t in self.tasks if t.priority == priority]

    def get_overdue_tasks(self, current_date):
        # упрощённо: если дата в формате "2026-04-10"
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
    todo.add_task("Срочная задача", "Сделать прямо сейчас", "high")
    todo.add_task("Неважная задача", "Можно отложить", "low")
    todo.add_task("Сдать отчёт", "Подготовить документы", "2026-04-05")
    todo.add_task("Купить продукты", "Молоко, хлеб", "2026-04-12")

    print("\nПросроченные задачи:")
    for task in todo.get_overdue_tasks("2026-04-10"):
        print(f"  {task}")
        
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