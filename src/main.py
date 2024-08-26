from task import Task

def main():
    t = Task()
    print("Enter 1 to add and 2 to show tasks and 0 to exit \n")
    while True:
        try:
            value = int(input("Enter value: "))
        except:
            print("Entered wrong input")
        if(value == 1):
            t.add_task_in_file()
        if(value == 2):
            t.delete_task()
        if(value == 3):
            t.mark_status()
        if(value == 4):
            t.get_tasks()
        if(value == 0):
            t.terminate()
            print("Program exited")
            break
        else:
            print("Please enter either 1 or 0.")

if __name__ == "__main__":
    main()
