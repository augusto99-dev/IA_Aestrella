import PySimpleGUI as sg

from controllers.AStarController import AStarController

class CargarCantidadNodos():
        def __init__(self, controller: AStarController) -> None:
            self.controller = controller
        nodos_array = []
        def create(self):
                layout = [[sg.Text("Cantidad de Nodos: "), sg.Input(key='-Nodo_cant-', do_not_clear=True, size=(10, 1))],
                        [sg.Button('Aceptar'), sg.Exit()]]
                
                window = sg.Window("Cargar Cantidad de nodos Aleatorios",layout, modal=True)

                while True:
                        event, values = window.read()
                        if event == "Exit" or event == sg.WIN_CLOSED:
                                break
                        if event == 'Aceptar':
                                cant = values['-Nodo_cant-']
                                self.nodos_array = self.controller.random_nodes(cant)
                                break
                window.close()
                return self.nodos_array 