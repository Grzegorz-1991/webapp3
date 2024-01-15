import functions
import PySimpleGUI as sg

# Window content
label = sg.Text('Type in a to-do')
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button('Add')

layout = [[label], [input_box, add_button]]

# Create the window
window = sg.Window('My To-Do App', layout)

event, values = window.read()

print('Hello',values[0], "! Dzieki za skorzystanie z czegos tam")

window.close()

