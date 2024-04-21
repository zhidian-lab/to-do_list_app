import PySimpleGUI as sg

layout = []
# append Add feature
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to-do")
input_button = sg.Button("Save")
layout.append([label, input_box, input_button])

# display the gui
window = sg.Window("My To-Do App", layout = layout)
print(help(window.read))
window.read()
window.close()