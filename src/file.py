import json
import os

# print("Current Working Directory:", os.getcwd())

file_path = 'file.json'
task_list = []
task_counter = 0

try:
    with open(file_path, 'r') as file:
        task_list = json.load(file)
        task_counter = len(task_list)
except FileNotFoundError:
    print(f"Error: The file '{file_path}' does not exist.")
except json.JSONDecodeError:
    print("Error: The file contains invalid JSON.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# print("Task List:", task_list)
# print("Task Counter:", task_counter)

tasks = [
    {'taskId': 1, 'markCompleted' : False},
    {'taskId': 2, 'markCompleted' : False},
    {'taskId': 3, 'markCompleted' : False},
    {'taskId': 4, 'markCompleted' : False},
    {'taskId': 5, 'markCompleted' : False},
    {'taskId': 6, 'markCompleted' : False},
]

letId = 3

# task_list = [task for task in task_list if task['taskId'] != letId]
# id_get = map(lambda task: if task['taskId'] == letId: task['markCompleted'] = True, tasks)
status = [task['markCompleted'] for task in tasks if task['taskId'] == letId]

print(status)


def inc(task):
    # Extract the taskId from the dictionary
    taskId = task['taskId']
    taskName = task['taskName']
    taskDesc = task['taskDesc']
    # Increment taskId if it is greater than letId
    if taskId > letId:
        return {'taskId': taskId - 1, 'taskName': taskName, 'taskDesc': taskDesc}
    # Return the original task if no change
    return task

# upd_data = map(inc, task_list)
# updated_tasks = list(upd_data)
# # task_list = [task['taskId'] for task in task_list if ]
# for task in updated_tasks:
#     print(task)
#
# with open(file_path, 'w') as file:
#     json.dump(updated_tasks, file, indent=4)
# print(updated_tasks)