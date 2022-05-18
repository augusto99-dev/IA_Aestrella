from typing import List
import PySimpleGUI as sg
import os.path
from views.ViewCargarNodos import CargarNodos
from views.ViewCargarArista import CargarArista
from views.ShowResult import ShowResult
from views.ViewOrigenDestino import CargarOrigenDestino
from controllers.AStarController import AStarController


class ViewPrincipal():
    img = "descarga.png"
    img_preview = "descarga.png"
    nodos_array = []
    combo_array = []
    aristas_array = []
    headings = ['Nodo', 'Heuristica']
    headings_arista = ['Nodo Inicial', 'Nodo Final', 'Costo']
    #view_cargarnodo = CargarNodos()
    #view_cargararista = CargarArista()

    def __init__(self, controller: AStarController) -> None:
        self.controller = controller
        self.view_cargarnodo = CargarNodos(controller)
        self.view_cargararista = CargarArista(controller)
        self.view_cargarOrigen = CargarOrigenDestino(controller)
        self.view_showresult = ShowResult()
        self.img_preview = "descarga.png"
        self.layout2 = [
            [sg.Table(values=self.nodos_array, headings=self.headings, max_col_width=35,
                      auto_size_columns=True,
                      display_row_numbers=False,
                      justification='center',
                      num_rows=10,
                      enable_events=True,
                      key='-NODE_TABLE-',
                      row_height=35,
                      tooltip='Tabla de Nodos')],
            [sg.Button('Insertar'), sg.Button('Cargar Relaciones'), sg.Button('Cancelar Carga')]
        ]
        self.layout3 = [
                    [sg.Table(values=self.aristas_array, headings=self.headings_arista, max_col_width=35,
                      auto_size_columns=True,
                      display_row_numbers=False,
                      justification='center',
                      num_rows=10,
                      enable_events=True,
                      key='-EDGE_TABLE-',
                      row_height=35,
                      tooltip='Tabla de Aristas')],
            [sg.Button('Insertar Arista'),sg.Button('Definir Origen/Destino'), sg.Button('Terminar Carga'), sg.Button('Cancelar Carga')]
        ]
        self.layout4 = [
            [sg.Image(self.img_preview, key='-IMG_PREV-',expand_x=True)],
            [sg.Button('Resultado Directo'), sg.Button('Paso a paso')]
        ]
        self.layout1 = [
            [sg.Image(self.img, expand_x=True)],
            [sg.Button('Cargar Datos')]
        ]

        self.layout = [[sg.Column(self.layout1, key='-COL1-'), sg.Column(self.layout2, visible=False, key='-COL2-'),
                   sg.Column(self.layout3, visible=False, key='-COL3-')
                      , sg.Column(self.layout4, visible=False, key='-COL4-')],
                  [sg.Button('Exit')]]

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
            elif event == 'Definir Origen/Destino':
                self.view_cargarOrigen.create(self.combo_array)
            elif event == 'Insertar':
                nodo = self.view_cargarnodo.create()
                print('nodo: ', nodo)
                self.nodos_array.append(nodo)
                self.combo_array.append(nodo[0])
                window['-NODE_TABLE-'].update(self.nodos_array)
            elif event == '-EDGE_TABLE-':
                selected_index = values['-EDGE_TABLE-'][0]
                selected_row = self.nodos_array[selected_index]
                popup_message = "Nodo: " + selected_row[0] + "\n" + "Heuristica: " + selected_row[1]
                sg.popup(popup_message)
            elif event == 'Insertar Arista':
                arista = self.view_cargararista.create(self.combo_array)
                self.aristas_array.append(arista)
                window['-EDGE_TABLE-'].update(self.aristas_array)
            elif event == '-EDGE_TABLE-':
                selected_index = values['-EDGE_TABLE-'][0]
                print('selected_index')
                print(selected_index)
                sel_row = self.aristas_array[selected_index]
                print('sel_row')
                print(sel_row)
                popup_message = "Nodo Incial: " + sel_row[0] + "\n" + "Nodo Final: " + sel_row[1]+ "\n" + "Costo: " + sel_row[2]
                sg.popup(popup_message)
            elif event == 'Cancelar Carga':
                window['-COL2-'].update(visible=False)
                window['-COL3-'].update(visible=False)
                window['-COL1-'].update(visible=True)
            elif event == 'Terminar Carga':
                window['-COL3-'].update(visible=False)
                window['-COL4-'].update(visible=True)
                window['-IMG_PREV-'].update(self.controller.getPreviewPath())
            elif event == 'Paso a paso':
                self.view_showresult.showresult("Paso a paso", self.img, "aa")
            elif event == 'Resultado Directo':
                img_path = self.controller.get_path_last_step()
                self.view_showresult.showresult("Resultado Directo", img_path, "")
            # window.close()

