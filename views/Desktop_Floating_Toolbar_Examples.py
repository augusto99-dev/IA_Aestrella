import PySimpleGUI as sg

from controllers.AStarController import AStarController
from examples.Test import Test
from examples.Test2 import Test2

from views.ViewPrincipal import ViewPrincipal


class ExamplesController:
    def __init__(self):
        pass

    def launch_examples_view(self):
        # sg.theme('Dark')

        # sg.set_options(element_padding=(0, 0),
        #               button_element_size=(12, 1), auto_size_buttons=False)

        layout = [[sg.Button('Ejemplo 1', button_color=('white', '#35008B')),
                   sg.Button('Ejemplo 2', button_color=('white', '#35008B')),
                   # sg.Button('Ejemplo 3', button_color=('white', '#35008B')),
                   sg.Button('EXIT', button_color=('white', 'firebrick3'))],
                  [sg.Text('', text_color='white', size=(50, 1), key='output')]]

        window = sg.Window('Ejemplos',
                           layout,
                           no_titlebar=True,
                           grab_anywhere=True,
                           keep_on_top=True)

        # ---===--- Loop taking in user input and executing appropriate program --- #
        while True:
            event, values = window.read()
            if event == 'EXIT' or event == sg.WIN_CLOSED:
                break  # exit button clicked
            if event == 'Ejemplo 1':
                print('Run your program 1 here!')
                controller: AStarController = AStarController()
                controller.reset_values()
                test = Test(controller)
                view_principal = ViewPrincipal(controller)
                view_principal.launch_preview_example()


            elif event == 'Ejemplo 2':
                print('Run your program 2 here!')
                controller_example2: AStarController = AStarController()
                controller_example2.reset_values()
                test = Test2(controller_example2)
                view_principal = ViewPrincipal(controller_example2)
                view_principal.launch_preview_example()

            elif event == 'Ejemplo 2':
                print('Run your program 2 here!')
            else:
                print(event)

        window.close()

