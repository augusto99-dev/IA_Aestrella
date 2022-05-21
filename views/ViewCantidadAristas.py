import PySimpleGUI as sg

from controllers.AStarController import AStarController

class CargarCantidadAristas():
        def __init__(self, controller: AStarController) -> None:
            self.controller = controller
        nodos_array = []
        def create(self):
                layout = [[sg.Text("Cantidad de Relaciones: "), sg.Input(key='-Edge_cant-', do_not_clear=True, size=(10, 1))],
                        [sg.Button('Aceptar'), sg.Exit()]]
                
                window = sg.Window("Cargar Cantidad Aristas Aleatorios",layout, modal=True)

                while True:
                        event, values = window.read()
                        if event == "Exit" or event == sg.WIN_CLOSED:
                                break
                        if event == 'Aceptar':
                                cant = values['-Edge_cant-']
                                self.edges_array = self.controller.random_edges(cant)
                                break
                window.close()
                return self.edges_array 