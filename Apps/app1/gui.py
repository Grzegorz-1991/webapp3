import functions
import PySimpleGUI as sg

# Window content
label = sg.Text('Type in a to-do')
input_box = sg.InputText(tooltip="Enter todo", key='todo')
add_button = sg.Button('Add')

layout = [[label], [input_box, add_button]]
font = 'Helvetica 20'

# Create the window
window = sg.Window('My To-Do App',
                   layout,
                   font=font)

while True:
    event, values = window.read()

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()

