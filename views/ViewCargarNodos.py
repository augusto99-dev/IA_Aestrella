import PySimpleGUI as sg

from controllers.AStarController import AStarController


class CargarNodos():
        def __init__(self, controller: AStarController) -> None:
            self.controller = controller

        def create(self):
                nodo = None
                layout = [[sg.Text("Nodo"), sg.Input(key='-Nodo-', do_not_clear=True, size=(10, 1))],
                        [sg.Text("Heuristica"), sg.Input(key='-Heuristica-', do_not_clear=True, size=(10, 1))],
                        [sg.Button('Insertar'), sg.Exit()]]
                window = sg.Window("Cargar Nodo",layout, modal=True)

                while True:
                        event, values = window.read()
                        if event == "Exit" or event == sg.WIN_CLOSED:
                                break
                        if event == 'Insertar':
                                nodo = [values['-Nodo-'], values['-Heuristica-']]
                                self.controller.add_node(values['-Nodo-'], values['-Heuristica-'])
                                break
                window.close()
                return nodo
                
                                

