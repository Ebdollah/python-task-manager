
# Task Manager

A simple command-line interface (CLI) application to manage tasks. The application allows users to add, delete, and mark tasks as completed. Tasks are persisted in a JSON file to retain data between runs.

## Requirements

- **Python Version**: Python 3.10+
- **Code Quality**: PEP-8 guidelines followed

## Project Structure

```plaintext
task-manager/
    |_ README.md
    |_ src/
        |_ __init__.py
        |_ main.py
        |_ task.py
        |_ utils.py
```

## How to Run

1. **Clone the Repository**: First, clone this repository to your local machine.

   ```bash
   git clone https://github.com/Ebdollah/python-task-manager
   ```

2. **Navigate to the `src/` Directory**:

   ```bash
   cd task-manager/src
   ```

3. **Run the Application**:

   Run the application using the following command:

   ```bash
   python main.py
   ```

## Features

1. **Add Task**: 
   - Allows the user to add a new task with a unique ID, task name, and description.

2. **Delete Task**: 
   - Enables the user to delete a task by specifying its ID.

3. **Mark Task as Completed**: 
   - Provides the functionality to mark a task as completed by specifying its ID.

4. **List Tasks**: 
   - Lists all tasks, with completed tasks clearly indicated as "Completed" and others as "Incomplete".

5. **Exit**: 
   - Saves all tasks to a JSON file and exits the program.

## Code Explanation

- **main.py**: 
  - This is the entry point of the application. It presents a menu to the user and executes actions based on the user’s input.

- **task.py**: 
  - Contains the `Task` class, which manages tasks, including adding, deleting, marking as completed, and listing tasks.
  - It handles the persistence of tasks by reading from and writing to a JSON file.

- **utils.py**: 
  - Contains utility functions, such as generating a short UUID for task IDs.

## Example Usage

When you run the application, you will see a menu like this:

```plaintext
Task Manager
1. Add Task
2. Delete Task
3. Mark Task as Completed
4. List Tasks
5. Exit
Choose an option:
```

You can choose an option by entering the corresponding number. 

### Adding a Task

If you choose to add a task (Option 1), you will be prompted to enter the task name and description. The task will be added to the task list and saved to `example.json`.

### Deleting a Task

If you choose to delete a task (Option 2), you will be asked to enter the Task ID of the task you wish to delete.

### Marking a Task as Completed

If you choose to mark a task as completed (Option 3), you will be asked to enter the Task ID of the task you wish to mark as completed.

### Listing Tasks

If you choose to list tasks (Option 4), all tasks will be displayed along with their status (Completed or Incomplete).

### Exiting the Program

If you choose to exit (Option 5), all tasks will be saved, and the program will terminate.

## Notes

- **Persistence**: Tasks are stored in `example.json` located in the `src/` directory. This ensures that tasks are retained between runs of the program.
- **Python Version**: Ensure that you are using Python 3.10+ to run this code.
- **Code Quality**: The code follows PEP-8 guidelines for improved readability and maintainability.
