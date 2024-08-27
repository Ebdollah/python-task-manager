from typing import List
from task import Task
import utils

class TaskManager:
    def __init__(self, file_path: str = 'example.json'):
        self.file_path = file_path
        task_dicts = utils.load_tasks_from_file(self.file_path)
        self.task_list: List[Task] = [Task(**task) for task in task_dicts]

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
                print(f"ID: {task.taskId} | Name: {task.taskName} | Description: {task.taskDesc} | Status: {'Completed' if task.markCompleted else 'Pending'}")
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
        utils.save_tasks_to_file(self.file_path, self.task_list)

    def terminate(self):
        print("All tasks saved and program exited.")
