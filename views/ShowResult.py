from textwrap import wrap
import PySimpleGUI as sg

# from controllers.AStarController import AStarController


class ShowResult():

    def __init__(self):
        # self.controller = controller
        pass

    def showresult(self, title, img, message):
        width = 70
        lines = list(map(lambda line: wrap(line, width=width), message.split('\n')))
        height = sum(map(len, lines))

        message = '\n'.join(map('\n'.join, lines))

        layout = [
            [sg.Image(img, expand_x=True)],
            [sg.Text(message, size=(width, height), justification='center', expand_x=True)]
        ]

        window = sg.Window(title, layout, keep_on_top=True, resizable=True).Finalize()
