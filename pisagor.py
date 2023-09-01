import math
import random

import PySimpleGUI as sg
color=["red","blue","purple","black","pink","orange","brown"]
label=sg.Text("1.KENAR")
inp=sg.InputText(tooltip="give an input",key="ONE")
label1=sg.Text("2.KENAR")
inp1=sg.InputText(tooltip="give an input",key="SECOND")
add_button=sg.Button("button" )
labellistb1=sg.Text("first number")
chos=random.choice(color)
lst = sg.Listbox([], size=(6, 4), font=('Arial Bold', 14), expand_y=True, enable_events=True, key='-LIST-',text_color=chos )
labellistb2=sg.Text("second number")
lst2 = sg.Listbox([], size=(6, 4), font=('Arial Bold', 14), expand_y=True, enable_events=True, key='-LIST1-',text_color=chos)
labellistb3=sg.Text("result number")
lst3 = sg.Listbox([], size=(6, 4), font=('Arial Bold', 14), expand_y=True, enable_events=True, key='-LIST2-',text_color=chos)
win=sg.Window("my application",layout=[[label,inp] ,[label1,inp1],[add_button],[labellistb1,labellistb2,labellistb3],[lst,lst2,lst3]])
liste=list()
liste1=list()
liste2=list()
while True:
    event, values = win.read()
    print(event)
    if event=='button':
        t=math.sqrt(int(values["ONE"])**2+int(values["SECOND"])**2)
        liste.append(values["ONE"])
        liste1.append(values["SECOND"])
        liste2.append(t)
        win["-LIST-"].update(values=liste )
        win["-LIST1-"].update(values=liste1, )
        win["-LIST2-"].update(values=liste2, )
    elif event==sg.WIN_CLOSED:
        break
win.close()