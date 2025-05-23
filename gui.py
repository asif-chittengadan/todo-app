import function
import FreeSimpleGUI as sg
import time

sg.theme("DarkBlack1")

clock=sg.Text('', key="clock")
label =sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter a todo", key="todo")
list_box = sg.Listbox(values=function.get_todos(), key='todos',
                      enable_events=True, size=[45,10])
add_button=sg.Button("Add")
edit_button=sg.Button("Edit")
complete_button=sg.Button("Complete")
exit_button=sg.Button("Exit")

window = sg.Window('My To-Do App',
                   layout=[[clock],
                           [label],
                           [input_box,add_button],
                           [list_box, edit_button,complete_button],
                           [exit_button]],
                   font=('Helvetica', 20))
while True:
    event, values = window.read(timeout=10)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(event)
    print(values)
    match event:
        case "Add":
            todos=function.get_todos()
            new_todo=values['todo'] + '\n'
            todos.append(new_todo)
            function.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_edit = values['todos'][0]
                new_todo = values['todo']

                todos = function.get_todos()
                index = todos.index(todo_edit)
                todos[index]=new_todo
                function.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first", font=('Helvetica', 20))
        case "Complete":
            try:
                todo_complete=values['todos'][0]
                todos=function.get_todos()
                todos.remove(todo_complete)
                function.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first", font=('Helvetica', 20))
        case "Exit":
            break
        case "todos":
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break
window.close()