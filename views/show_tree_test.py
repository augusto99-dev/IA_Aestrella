from textwrap import wrap
import PySimpleGUI as sg


class Step_to_step:
    def __init__(self):
        pass


    def steptostep(self, title, img, message, width=70):
        lines = list(map(lambda line:wrap(line, width=width), message.split('\n')))
        height = sum(map(len, lines))

        message = '\n'.join(map('\n'.join, lines))

        layout = [
            [sg.Image(img,expand_x=True)],
            [sg.Text(message, size=(width, height), justification='center', expand_x=True)],
            [sg.Button('Next Step')]
        ]

        sg.Window(title, layout, keep_on_top=True, modal=True).read(close=2000)
