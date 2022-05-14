import PySimpleGUI as sg
import ViewTablaNodos

information_array = []
headings = ['NODO', 'HEURISTICA']

layout = [[sg.Text("Nodo"), sg.Input(key='-Nodo-', do_not_clear=True, size=(10, 1))],
          [sg.Text("Heuristica"), sg.Input(key='-Heuristica-', do_not_clear=True, size=(10, 1))],
          [sg.Button('Insertar'), sg.Button('Mostrar tabla'), sg.Exit()]]

window = sg.Window("Insertar", layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
            break
    elif event == 'Insertar':
            contact_information = [values['-Nodo-'], values['-Heuristica-']]
            information_array.append(contact_information)
            sg.popup("Datos Ingresados")
    elif event == 'Mostrar tabla':
            ViewTablaNodos.create(information_array, headings)
