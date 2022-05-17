from typing import List
import PySimpleGUI as sg
import os.path
from ViewCargarNodos import CargarNodos
from ShowResult import ShowResult
view_cargarnodo = CargarNodos()
view_showresult = ShowResult()
class ViewPrincipal():
    img = "/home/julio/Escritorio/IA_Aestrella/subarbol.png"
    nodos_array = []
    combo_array = []
    headings = ['Nodo', 'Heuristica']
    view_cargarnodo = CargarNodos()
    def __init__(self) -> None:
        pass
    def get_node_list(self)-> List:
        return self.nodos_array
    
    def get_combo_list(self)-> List:
        return self.nodos_array
    layout2 = [
                [sg.Table(values=nodos_array, headings=headings, max_col_width=35,
                            auto_size_columns=True,
                            display_row_numbers=False,
                            justification='right',
                            num_rows=10,
                            enable_events=True,
                            key='-CONTACT_TABLE-',
                            row_height=35,
                            tooltip='Reservations Table')],
                [sg.Button('Insertar'), sg.Button('Cargar Relaciones'), sg.Button('Cancelar Carga')]
            ]
    layout3 = [
                [sg.Text('Nodo Origen: '),sg.Combo(combo_array,
                            size=(5,1),
                            key='-FROM-NODE-'),
                sg.Text('Nodo Destino: '),sg.Combo(combo_array,
                            size=(5,1),
                            key='-TO-NODE-'),
                sg.Text('Heuristica', size=(10,1)), sg.InputText(key="lp1",size=(5,1))],
                [sg.Button('Terminar Carga'), sg.Button('Cancelar Carga')]
            ]
    layout4 = [
                [sg.Image(img,expand_x=True)],
                [sg.Button('Resultado Directo'), sg.Button('Paso a paso')]
            ]
    layout1 = [
            [sg.Image(img,expand_x=True)],
            [sg.Button('Cargar Datos')]
        ]


    layout = [[sg.Column(layout1, key='-COL1-'), sg.Column(layout2, visible=False, key='-COL2-'), sg.Column(layout3, visible=False, key='-COL3-')
    , sg.Column(layout4, visible=False, key='-COL4-')],
            [sg.Button('Exit')]]

    window = sg.Window("TP Final Inteligencia Artificial", layout,).Finalize()
    window.Maximize()
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        elif event == 'Cargar Datos':
            window['-COL1-'].update(visible=False)
            window['-COL2-'].update(visible=True)
        elif event == 'Cargar Relaciones':
            window['-COL2-'].update(visible=False)
            window['-COL3-'].update(visible=True)
        elif event == 'Insertar':
                    nodo = view_cargarnodo.create()
                    nodos_array.append(nodo)
                    combo_array.append(nodo[0])
                    window['-CONTACT_TABLE-'].update(nodos_array)
        elif event == '-CONTACT_TABLE-':
                    selected_index = values['-CONTACT_TABLE-'][0]
                    selected_row = nodos_array[selected_index]
                    popup_message = "Nodo: " + selected_row[0] + "\n" + "Heuristica: " + selected_row[1]
                    sg.popup(popup_message)
        elif event == 'Cancelar Carga':
            window['-COL2-'].update(visible=False)
            window['-COL3-'].update(visible=False)
            window['-COL1-'].update(visible=True)
        elif event == 'Terminar Carga':
            window['-COL3-'].update(visible=False)
            window['-COL4-'].update(visible=True)

        elif event == 'Paso a paso':
            view_showresult.showresult("Paso a paso",img,"aa")
        elif event == 'Resultado Directo':
            view_showresult.showresult("Resultado Directo",img,"aa")

    window.close()