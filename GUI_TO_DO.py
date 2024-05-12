import function
import PySimpleGUI as sg

lable = sg.Text('Type in a to-do')
Button = sg.Button('Add')
User_input = sg.InputText(tooltip="type todo",key='todo')

window = sg.Window('My to-do App',
                   layout=[[lable],[User_input,Button]],
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

        case sg.WIN_CLOSED:
            break
window.close()