from task import TaskManager

def main():
    t = TaskManager()
    print("Task Manager")
    print("1. Add Task\n2. Delete Task\n3. Mark Task as Completed\n4. List Tasks\n5. Exit")
    while True:
        try:
            value = int(input("Choose an option: "))
        except ValueError:
            print("Invalid choice. Please try again.")
            continue

        if value == 1:
            t.add_task_in_file()
        elif value == 2:
            t.delete_task()
        elif value == 3:
            t.mark_status()
        elif value == 4:
            t.get_tasks()
        elif value == 5:
            t.terminate()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
