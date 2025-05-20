import function
import time

now=time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action=input("type add,show,edit,complete or exit :")
    user_action=user_action.strip()
    if user_action.startswith('add'):
        todo=user_action[4:]

        todos=function.get_todos()

        todos.append(todo + '\n')

        function.write_todos(todos)

    elif user_action.startswith('show'):

        todos = function.get_todos()

        for i,item in enumerate(todos):
            item=item.strip('\n')
            row=f"{i+1}-{item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number=int(user_action[5:])
            print(number)
            number=number-1

            todos = function.get_todos()

            new=input("enter the new todo :")
            todos[number]=new + '\n'

            function.write_todos(todos)
        except ValueError:
            print("wrong command !!")
            continue

    elif user_action.startswith('complete'):
        try:
            number=int(user_action[9:])

            todos = function.get_todos()

            index=number-1
            todo_to_remove=todos[index].strip('\n')
            todos.pop(index)

            function.write_todos(todos)

            message=f"the todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("there is no item with that number")
            continue
    elif user_action.startswith('exit'):
        break
    else :
        print("command not valid")
print("bye")