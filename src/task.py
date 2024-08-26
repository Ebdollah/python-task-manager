import json
import uuid

class Task:
    task_counter = 0

    def __init__(self):
        self.file_path = 'example.json'
        try:
            with open(self.file_path, 'r') as file:
                self.task_list = json.load(file)
            Task.task_counter = len(self.task_list)
        except (FileNotFoundError, json.JSONDecodeError):
            self.task_list = []
    @staticmethod
    def generate_short_uuid():
        return str(uuid.uuid4().int)[:5]

    def add_task_in_file(self):
        task_namee = input("Task Name: ")
        task_desc = input("Task description: ")
        task_id = self.generate_short_uuid()
        newDict = {
            "taskId": task_id,
            "taskName": task_namee,
            "taskDesc": task_desc,
            "markCompleted" : False
        }
        self.task_list.append(newDict)
        with open(self.file_path, 'w') as file:
            json.dump(self.task_list, file, indent=4)
        Task.task_counter += 1
    
    def get_tasks(self):
        for task in self.task_list:
            print(task)

    def delete_task(self):
        taskId = (input("Enter Task Id: "))
        self.task_list = [task for task in self.task_list if taskId != task['taskId']]
        # upd_data = map(lambda task: self.inc(task, taskId), self.task_list)
        # self.task_list = list(upd_data)
        with open(self.file_path, 'w') as file:
            json.dump(self.task_list, file, indent=4)

    @staticmethod
    def inc(task, letId):
        # Extract tasks seperately from the dictionary
        taskId = task['taskId']
        taskName = task['taskName']
        taskDesc = task['taskDesc']
        taskStatus = task['markCompleted']
        # Increment taskId if it is greater than letId
        if taskId > letId:
            return {'taskId': taskId - 1, 'taskName': taskName, 'taskDesc': taskDesc, 'markCompleted': taskStatus}
        # Return the original task if no change
        return task

    def mark_status(self):
        taskID = int(input("Enter Task Id: "))
        # self.task_list = [task['markCompleted'] for task in self.task_list if taskID == task['taskId']]
        self.task_list = list(map(lambda task: self.mark_completed(task,taskID), self.task_list))
        with open(self.file_path, 'w') as file:
            json.dump(self.task_list, file, indent=4)

    @staticmethod
    def mark_completed(task, letId):
        # Create a new dictionary with the updated 'markCompleted' value if the condition is met
        if task['taskId'] == letId:
            task = task.copy()  # Create a copy to avoid mutating the original dictionary
            task['markCompleted'] = True
        return task

    def terminate(self):
        print("All tasks saved and program exited.")
# import json
# class Task:
#     # task_list = []
#     task_counter = 0
#     # file = open('example.json', 'a')
#     # file.write([])

    
#     def _init_(self, task_name = '', task_disc = '') -> None:
#         try:
#             with open('example.json', 'r') as file:
#                 self.task_list = json.load(file)
#             Task.task_counter = len(self.task_list)
#         except (FileNotFoundError, json.JSONDecodeError):
#             self.task_list = []
#         self.id = Task.task_counter
#         self.name = task_name
#         self.description = task_disc
#         # Task.task_counter += 1
#         # Task.task_list.append(tuple(task_name, task_disc))
    
#     # def add_task(self):
#     #     task_namee = input("Task Name: ")
#     #     task_desc = input("Task description: ")
#     #     task_id = Task.task_counter
#     #     # Task.task_list.append([task_id, task_namee, task_desc])
#     #     Task.task_list.append(
#     #         {
#     #             "taskId" : task_id,
#     #             "taskName" : task_namee,
#     #             "taskDesc" : task_desc
#     #         }
#     #     )
#     #     Task.task_counter += 1 
    
#     # def add_task_in_file(self):
#     #     task_namee = input("Task Name: ")
#     #     task_desc = input("Task description: ")
#     #     task_id = Task.task_counter
#     #     newDict = {
#     #             "taskId" : task_id,
#     #             "taskName" : task_namee,
#     #             "taskDesc" : task_desc
#     #         }
#     #     # Task.task_list.append(newDict)
#     #     # file = open('example.json', 'a')
#     #     Task.file.write(
#     #             json.dumps(newDict) + "\n"
#     #         )
#     #     # file.close()
#     #     Task.task_counter += 1 

#     def add_task_in_file(self):
#         task_name = input("Task Name: ")
#         task_desc = input("Task description: ")
#         task_id = Task.task_counter

#         # Creating a new task dictionary
#         new_task = {
#             "taskId": task_id,
#             "taskName": task_name,
#             "taskDesc": task_desc
#         }

#         # Adding the new task to the task list
#         self.task_list.append(new_task)

#         # Incrementing the task counter
#         Task.task_counter += 1

#     def save_tasks_to_file(self):
#         # Saving the task list to a JSON file
#         with open('example.json', 'w') as file:
#             json.dump(self.task_list, file, indent=4)
    
#     # def get_tasks(self):
#     #     for task in Task.task_list:
#     #         print(task)

#     # def get_by_id(self):
#     #     t_id = int(input("Enter ID of task: "))
#     #     return [task for task in Task.task_list if t_id == task['taskId']]
    
#     def terminate(self):
#         self.save_tasks_to_file()
        