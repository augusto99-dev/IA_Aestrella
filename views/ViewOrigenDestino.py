import PySimpleGUI as sg

from controllers.AStarController import AStarController

class CargarOrigenDestino():
        def __init__(self, controller: AStarController) -> None:
            self.controller = controller
        def create(self,array_nodo):
                layout = [[sg.Text("Nodo Origen"), sg.Combo(array_nodo, key='-nodo_origen-', size=(10, 1))],
                        [sg.Text("Nodo Destino: "), sg.Combo(array_nodo, key='-nodo_destino-', size=(10, 1))],
                        [sg.Button('Aceptar'), sg.Exit()]]
                
                window = sg.Window("Cargar Nodo",layout, modal=True)

                while True:
                        event, values = window.read()
                        if event == "Exit" or event == sg.WIN_CLOSED:
                                break
                        if event == 'Aceptar':
                                nodos = [values['-nodo_origen-'], values['-nodo_destino-']]
                                self.controller.set_origin(nodos[0])
                                self.controller.set_origin(nodos[1])
                                break
                window.close()