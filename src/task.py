import json
from utils import generate_short_uuid

class Task:
    def __init__(self):
        self.file_path = 'example.json'
        try:
            with open(self.file_path, 'r') as file:
                self.task_list = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.task_list = []

    def add_task_in_file(self):
        task_name = input("Task Name: ")
        task_desc = input("Task Description: ")
        task_id = generate_short_uuid()
        new_task = {
            "taskId": task_id,
            "taskName": task_name,
            "taskDesc": task_desc,
            "markCompleted": False
        }
        self.task_list.append(new_task)
        self.save_tasks()

    def get_tasks(self):
        if not self.task_list:
            print("No tasks available.")
        for task in self.task_list:
            status = "Completed" if task["markCompleted"] else "Incomplete"
            print(f"ID: {task['taskId']}, Name: {task['taskName']}, Description: {task['taskDesc']}, Status: {status}")

    def delete_task(self):
        task_id = input("Enter Task ID to delete: ")
        self.task_list = [task for task in self.task_list if task['taskId'] != task_id]
        self.save_tasks()

    def mark_status(self):
        task_id = input("Enter Task ID to mark as completed: ")
        for task in self.task_list:
            if task['taskId'] == task_id:
                task['markCompleted'] = True
        self.save_tasks()

    def save_tasks(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.task_list, file, indent=4)

    def terminate(self):
        self.save_tasks()
        print("All tasks saved. Exiting the program.")
