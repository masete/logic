from tasks import todo_list, create_task, delete_task, delete_all_tasks, mark_as_finished
from accounts import users_list, add_account, login


options = """
   1. creating a task
   2. deleting a task
   3. deleting all tasks
   4. Marking a task finished
   0. To exit the program.
   """


def controller():
    """
        Allows a user to choose from a wide range of tasks and performs a task in response to
        the selected option.
    """
    print(f"{options}")
    selection = int(input("Make a selection: "))

    if selection and selection == 1:
        task_title = str(input("Enter a title: "))
        task_description = str(input("Enter a description: "))

        if task_title and task_title != " ":
            create_task(task_title, task_description)
            print("Task successfully created.")
            print(f"You currently have: {len(todo_list)} items in your todo-list")

    elif selection and selection == 2:
        task = int(input("Enter task to be deleted: "))
        deleted = delete_task(int(task))
        print(deleted)
        

    elif selection and selection == 3:
        delete_all = delete_all_tasks()
        print(delete_all)

    elif selection and selection == 4:
        task = input("Enter task to Finish: ")
        marked = mark_as_finished(int(task))
        print(marked)

    elif selection == 0:
        quit()

    else:
        controller()

    controller()


if __name__ == "__main__":
    name = input("Enter username ")

    while name in users_list:
        password = input("Enter password ")

        # login
        if  login(name, password) == True:
            print("Welcome {}".format(name))
            controller()
        break
        # create account
    else:
        password = input("Choose password ")
        add_account(name, password)
        controller()
