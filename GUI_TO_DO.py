import function
import PySimpleGUI as sg

lable = sg.Text('Type in a to-do')
Button = sg.Button('add')
User_input = sg.InputText(tooltip="type todo")

window = sg.Window('My to-do App', layout=[[lable],[User_input,Button]])
window.read()
window.close()