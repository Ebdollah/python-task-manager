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
        except FileNotFoundError:
            print(f"File '{self.file_path}' not found. Starting with an empty task list.")
            self.task_list = []
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from file '{self.file_path}': {e}")
            self.task_list = []
        except Exception as e:
            print(f"An unexpected error occurred while initializing tasks: {e}")
            self.task_list = []

    def add_task_in_file(self):
        try:
            task_name = input("Task Name: ")
            task_desc = input("Task description: ")
            task_id = Task.generate_short_uuid()
            new_task = Task(taskId=task_id, taskName=task_name, taskDesc=task_desc)
            self.task_list.append(new_task)
            self.save_tasks()
        except Exception as e:
            print(f"An error occurred while adding a task: {e}")

    def get_tasks(self):
        try:
            if not self.task_list:
                print("No tasks available.")
            for task in self.task_list:
                print(f"ID: {task.taskId} | Name: {task.taskName} | Description: {task.taskDesc} | Status: {task.markCompleted}")

                # print(task)
        except Exception as e:
            print(f"An error occurred while retrieving tasks: {e}")

    def delete_task(self):
        try:
            task_id = input("Enter Task Id: ")
            self.task_list = [task for task in self.task_list if task.taskId != task_id]
            self.save_tasks()
        except Exception as e:
            print(f"An error occurred while deleting the task: {e}")

    def mark_status(self):
        try:
            task_id = input("Enter Task Id: ")
            for task in self.task_list:
                if task.taskId == task_id:
                    task.markCompleted = True
                    break
            else:
                print(f"Task with Id '{task_id}' not found.")
            self.save_tasks()
        except Exception as e:
            print(f"An error occurred while marking the task status: {e}")

    def save_tasks(self):
        try:
            with open(self.file_path, 'w') as file:
                json.dump([task.__dict__ for task in self.task_list], file, indent=4)
        except IOError as e:
            print(f"An error occurred while saving tasks to file '{self.file_path}': {e}")
        except Exception as e:
            print(f"An unexpected error occurred while saving tasks: {e}")

    def terminate(self):
        print("All tasks saved and program exited.")
