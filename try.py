import PySimpleGUI as sg
label=sg.Text(" what is problem")
inp=sg.InputText(tooltip="give an input",key="todo")
add_button=sg.Button("button")
win=sg.Window("my application",layout=[[label,inp,add_button]])

while True:
    event, values = win.read()
    if event=='button':
        print(values)
    elif event==sg.WIN_CLOSED:
        break
        print(123)
win.close()