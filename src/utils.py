import json

def load_tasks_from_file(file_path: str):
    try:
        with open(file_path, 'r') as file:
            tasks = json.load(file)
            return tasks
    except FileNotFoundError:
        print(f"File '{file_path}' not found. Starting with an empty task list.")
        return []
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from file '{file_path}': {e}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred while loading tasks: {e}")
        return []

def save_tasks_to_file(file_path: str, task_list):
    try:
        with open(file_path, 'w') as file:
            json.dump([task.__dict__ for task in task_list], file, indent=4)
    except IOError as e:
        print(f"An error occurred while saving tasks to file '{file_path}': {e}")
    except Exception as e:
        print(f"An unexpected error occurred while saving tasks: {e}")
