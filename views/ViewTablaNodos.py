from typing import List
import PySimpleGUI as sg
from ViewCargarNodos import CargarNodos

class TablaNodos():

    def __init__(self) -> None:
        pass

    nodos_array = []
    headings = ['NODO', 'HEURISTICA']
    view_cargarnodo = CargarNodos()
    layout = [
            [sg.Table(values=nodos_array, headings=headings, max_col_width=35,
                        auto_size_columns=True,
                        display_row_numbers=False,
                        justification='right',
                        num_rows=10,
                        enable_events=True,
                        key='-CONTACT_TABLE-',
                        row_height=35,
                        tooltip='Reservations Table')],
            [sg.Button('Insertar'), sg.Button('Siguiente'), sg.Exit()]
        ]

    window = sg.Window("Tabla",layout, modal=True)

    while True:
            event, values = window.read()
            if event == "Exit" or event == sg.WIN_CLOSED:
                break
            if event == 'Insertar':
                nodo = view_cargarnodo.create()
                nodos_array.append(nodo)
                window['-CONTACT_TABLE-'].update(nodos_array)
            if event == '-CONTACT_TABLE-':
                selected_index = values['-CONTACT_TABLE-'][0]
                selected_row = nodos_array[selected_index]
                popup_message = "Nodo: " + selected_row[0] + "\n" + "Heuristica: " + selected_row[1]
                sg.popup(popup_message)
                        
    #window.close()
    def getLayout(self):
        return self.layout