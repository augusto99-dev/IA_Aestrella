import PySimpleGUI as sg


class ExamplesController:
    def __init__(self):
        pass

    def launch_examples_view(self):
        # sg.theme('Dark')

        # sg.set_options(element_padding=(0, 0),
        #               button_element_size=(12, 1), auto_size_buttons=False)

        layout = [[sg.Button('Ejemplo 1', button_color=('white', '#35008B')),
                   sg.Button('Ejemplo 2', button_color=('white', '#35008B')),
                   sg.Button('Ejemplo 3', button_color=('white', '#35008B')),
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
            elif event == 'Ejemplo 2':
                print('Run your program 2 here!')
            elif event == 'Ejemplo 2':
                print('Run your program 2 here!')
            else:
                print(event)

        window.close()

