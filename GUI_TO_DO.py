import function
import PySimpleGUI as sg

lable = sg.Text('Type in a to-do')
Button = sg.Button('Add')
User_input = sg.InputText(tooltip="type todo",key='todo')

Edit_button = sg.Button('Edit')
list_box = sg.Listbox(values=function.get_todos(),key='todos_list',enable_events=True, size=(45,10))

window = sg.Window('My to-do App',
                   layout=[[lable],[User_input,Button],[list_box,Edit_button]],
                   font=('Helvetica',20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = function.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            function.write_todos(todos)
            window['todos_list'].update(values=todos)


        case "Edit":
            todo_to_edit = values['todos_list'][0]
            new_todo = values['todo'] + "\n"
            todos = function.get_todos()

            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            function.write_todos(todos)
            window['todos_list'].update(values=todos)

        case "todos_list":
            window['todo'].update(value=values['todos_list'][0])

        case sg.WIN_CLOSED:
            break
window.close()