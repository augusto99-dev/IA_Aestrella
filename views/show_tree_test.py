from textwrap import wrap
import PySimpleGUI as sg


class Step_to_step:
    def __init__(self):
        pass


    def steptostep(self, number_step, img, message, width, height):
        # lines = list(map(lambda line:wrap(line, width=width), message.split('\n')))
        # height = sum(map(len, lines))
        #
        # message = '\n'.join(map('\n'.join, lines))
        #
        # layout = [
        #     [sg.Image(img,expand_x=True)],
        #     [sg.Text(message, size=(width, height), justification='center', expand_x=True)],
        #     [sg.Button('Paso Siguiente'), sg.Button('Paso Siguiente')],
        # ]
        lines = list(map(lambda line: wrap(line, width=width), message.split('\n')))
        height = sum(map(len, lines))
        layout = ''
        if number_step != 0:
            layout = [[sg.Image(img, expand_x=True)],
                      [sg.Text(message, size=(width, height), justification='center', expand_x=True)],
                      [sg.Button('Siguiente'), sg.Button('Anterior'), sg.Button('Cancel')]]
        else:
            layout = [[sg.Image(img, expand_x=True)],
                      [sg.Text(message, size=(width, height), justification='center', expand_x=True)],
                      [sg.Button('Siguiente'), sg.Button('Anterior', disabled=True), sg.Button('Cancel')]]

        # Create the Window
        window = sg.Window('PASO: ' + str(number_step), layout)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
                return 'exit'
                break
            elif event == 'Siguiente':  # if user closes window or clicks cancel
                # print('siguiente')
                window.close()
                return 'next'
                break
            elif event == 'Anterior':  # if user closes window or clicks cancel
                window.close()
                return 'back'
                break
            print('You entered ', values[0])



        window.close()

        # sg.Window(title, layout, keep_on_top=True, modal=True).read(close=2000)
