from typing import List
import PySimpleGUI as sg
import os.path
from views.ViewCargarNodos import CargarNodos
from views.ShowResult import ShowResult
from controllers.AStarController import AStarController


class ViewPrincipal():
    img = "descarga.png"
    nodos_array = []
    combo_array = []
    headings = ['Nodo', 'Heuristica']
    # view_cargarnodo = CargarNodos()

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
        [sg.Text('Nodo Origen: '), sg.Combo(combo_array,
                                            size=(5, 1),
                                            key='-FROM-NODE-'),
         sg.Text('Nodo Destino: '), sg.Combo(combo_array,
                                             size=(5, 1),
                                             key='-TO-NODE-'),
         sg.Text('Heuristica', size=(10, 1)), sg.InputText(key="lp1", size=(5, 1))],
        [sg.Button('Terminar Carga'), sg.Button('Cancelar Carga')]
    ]
    layout4 = [
        [sg.Image(img, expand_x=True)],
        [sg.Button('Resultado Directo'), sg.Button('Paso a paso')]
    ]
    layout1 = [
        [sg.Image(img, expand_x=True)],
        [sg.Button('Cargar Datos')]
    ]

    layout = [[sg.Column(layout1, key='-COL1-'), sg.Column(layout2, visible=False, key='-COL2-'),
               sg.Column(layout3, visible=False, key='-COL3-')
                  , sg.Column(layout4, visible=False, key='-COL4-')],
              [sg.Button('Exit')]]

    def __init__(self, controller: AStarController) -> None:
        self.controller = controller
        self.view_cargarnodo = CargarNodos(controller)
        self.view_showresult = ShowResult()

    def get_node_list(self) -> List:
        return self.nodos_array

    def get_combo_list(self) -> List:
        return self.nodos_array

    def launch_view(self):
        window = sg.Window("TP Final Inteligencia Artificial", self.layout, ).Finalize()

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
                print('nodos in cargar relaciones: ', self.controller.nodes)
            elif event == 'Insertar':
                nodo = self.view_cargarnodo.create()
                print('nodo: ', nodo)
                self.nodos_array.append(nodo)
                self.combo_array.append(nodo[0])
                window['-CONTACT_TABLE-'].update(self.nodos_array)
            elif event == '-CONTACT_TABLE-':
                selected_index = values['-CONTACT_TABLE-'][0]
                selected_row = self.nodos_array[selected_index]
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
                self.view_showresult.showresult("Paso a paso", self.img, "aa")
            elif event == 'Resultado Directo':
                self.view_showresult.showresult("Resultado Directo", self.img, "aa")
            # window.close()

