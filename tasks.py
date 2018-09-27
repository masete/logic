
# --- tasks.py ---
# This file contains code that manages your todo_list

todo1 = {'todo_id': 1,'todo_title':'fahad','todo_description':'andela','Finished':False}
todo2 = {'todo_id': 2,'todo_title':'joel','todo_description':'level','Finished':False}
todo_list = [todo1, todo2]


def create_task(task_title, task_description):
    todo = {}
    if not todo_list or task_title not in [todo.get('title', None) for todo in todo_list]:              
        todo["title"] = task_title
        todo["Description"] = task_description
        todo["todo_id"] = max([todo.get('todo_id', None) for todo in todo_list]) + 1 if todo_list else 1
        todo['Finished'] = False
        todo_list.append(todo)
        return todo_list    
    return "The task with the title {} already exists".format(task_title)
    
def search_todo_by_id(todo_id):
    if not todo_list:
        return 0
    for todo in todo_list:
        if todo_id == todo.get('todo_id'):
            return todo
    return 0

# Write a function deletes a task


def delete_task(todo_id):
    todo = search_todo_by_id(todo_id)
    if not todo:
        return "This todo does not exist"
    todo_title = todo.get('todo_title')
    todo_list.remove(todo)
    return "Task with title {} is deleted".format(todo_title) 




# Write a function that marks a task finished


def mark_as_finished(todo_id):
    todo = search_todo_by_id(todo_id)
    if not todo:
        return "This todo does not exist"
    if todo.get('Finished') is True:
        return "this todo ia already finished"
    todo['Finished'] = True
    return "{} has been finished".format(todo.get('todo_title'))
# Write a function deletes all tasks


def delete_all_tasks():
      if not todo_list:
          return "if todolist is empty"
      todo_list.clear()
      return "the todo list has been deleted"
    
