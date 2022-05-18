import PySimpleGUI as sg

from controllers.AStarController import AStarController
class CargarArista():
        def __init__(self, controller: AStarController) -> None:
            self.controller = controller
        def create(self,array_nodo):
                layout = [[sg.Text("Nodo Inicial: "), sg.Combo(array_nodo,key='-nodo_ini-', size=(10, 1))],
                        [sg.Text("Nodo Final: "), sg.Combo(array_nodo,key='-nodo_fin-', size=(10, 1))],
                        [sg.Text("Costo: "), sg.Input(key='-costo-', do_not_clear=True, size=(10, 1))],
                        [sg.Button('Insertar'), sg.Exit()]]
                
                window = sg.Window("Cargar Nodo",layout, modal=True)

                while True:
                        event, values = window.read()
                        if event == "Exit" or event == sg.WIN_CLOSED:
                                break
                        if event == 'Insertar':
                                arista = [values['-nodo_ini-'], values['-nodo_fin-'],values['-costo-']]
                                self.controller.add_edge(arista[0],arista[1],arista[2])
                                break
                window.close()
                return arista