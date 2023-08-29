import PySimpleGUI
label=PySimpleGUI.Text("YAZ BURAYA")
inp_box=PySimpleGUI.InputText(tooltip="enter ")
addbutton=PySimpleGUI.Button("TERT")
win=PySimpleGUI.Window('GUI',layout=[[label,inp_box,addbutton]])
win.read()
win.close()