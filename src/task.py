from dataclasses import dataclass, field
import json
import uuid
from typing import List

@dataclass
class Task:
    taskId: str
    taskName: str
    taskDesc: str
    markCompleted: bool = False

    @staticmethod
    def generate_short_uuid() -> str:
        return str(uuid.uuid4().int)[:5]

@dataclass
class TaskManager:
    file_path: str = 'example.json'
    task_list: List[Task] = field(default_factory=list)

    def __post_init__(self):
        try:
            with open(self.file_path, 'r') as file:
                tasks = json.load(file)
                self.task_list = [Task(**task) for task in tasks]
        except (FileNotFoundError, json.JSONDecodeError):
            self.task_list = []

    def add_task_in_file(self):
        task_name = input("Task Name: ")
        task_desc = input("Task description: ")
        task_id = Task.generate_short_uuid()
        new_task = Task(taskId=task_id, taskName=task_name, taskDesc=task_desc)
        self.task_list.append(new_task)
        self.save_tasks()

    def get_tasks(self):
        for task in self.task_list:
            print(task)

    def delete_task(self):
        taskId = input("Enter Task Id: ")
        self.task_list = [task for task in self.task_list if task.taskId != taskId]
        self.save_tasks()

    def mark_status(self):
        taskId = input("Enter Task Id: ")
        for task in self.task_list:
            if task.taskId == taskId:
                task.markCompleted = True
                break
        self.save_tasks()

    def save_tasks(self):
        with open(self.file_path, 'w') as file:
            json.dump([task.__dict__ for task in self.task_list], file, indent=4)

    def terminate(self):
        print("All tasks saved and program exited.")
