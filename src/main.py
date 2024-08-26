from task import Task

def main():
    task_manager = Task()
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Mark Task as Completed")
        print("4. List Tasks")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            task_manager.add_task_in_file()
        elif choice == '2':
            task_manager.delete_task()
        elif choice == '3':
            task_manager.mark_status()
        elif choice == '4':
            task_manager.get_tasks()
        elif choice == '5':
            task_manager.terminate()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
