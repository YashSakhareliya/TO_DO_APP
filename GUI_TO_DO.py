import function
import PySimpleGUI as sg
import time

sg.theme('DarkAmber')
clock = sg.Text(" ", key='clock')

lable = sg.Text('Type in a to-do')
Add_Button = sg.Button(image_size=(30,30),image_source="004 add.png",tooltip="Add Todo", mouseover_colors="LightBlue2", key="Add")
User_input = sg.InputText(tooltip="type todo", key='todo')

Edit_button = sg.Button('Edit')
list_box = sg.Listbox(values=function.get_todos(),key='todos_list',enable_events=True, size=(45,10))

complete_button =sg.Button(image_source="004 complete.png",tooltip="complete todo", mouseover_colors="LightBlue2", key="Complete", image_size=(70,50))
exit_button = sg.Button('Exit')

window = sg.Window('My to-do App',
                   layout=[[clock],
                           [lable],
                           [User_input, Add_Button],
                           [list_box, Edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=200)
    if event == sg.WIN_CLOSED:
        break
    window['clock'].update(value=time.strftime("IS NOW, %d %b - %Y, %I:%M:%S %p"))


    match event:
        case "Add":
            todos = function.get_todos()
            new_todo = values['todo'].strip()
            if new_todo == '':
                sg.popup("please enter to-do first   ",font=('Helvetica',20))
            else:
                todos.append(new_todo + "\n")
                function.write_todos(todos)
            window['todos_list'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['todos_list'][0]
                new_todo = values['todo'] + "\n"
                todos = function.get_todos()

                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                function.write_todos(todos)
                window['todos_list'].update(values=todos)
            except IndexError:
                sg.popup('please select item first',font=('Helvetica',20))

        case "todos_list":
            window['todo'].update(value=values['todos_list'][0])

        case "Complete":
            try:
                todo_to_complete = values['todos_list'][0]
                todos = function.get_todos()
                todos.remove(todo_to_complete)
                function.write_todos(todos)
                window['todos_list'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup('please select item first', font=('Helvetica', 20))

        case "Exit":
            break


window.close()