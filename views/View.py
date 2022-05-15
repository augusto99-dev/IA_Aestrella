from textwrap import wrap
import PySimpleGUI as sg

class View:
    def __int__(self, controller):
        '''

        Parameters
        ----------
        controller

        Returns
        -------

        '''


def steptostep(title,img,message,width=70):

    lines = list(map(lambda line:wrap(line, width=width), message.split('\n')))
    height = sum(map(len, lines))
    message = '\n'.join(map('\n'.join, lines))

    layout = [
        [sg.Image(img,expand_x=True)],
        [sg.Text(message, size=(width, height), justification='center', expand_x=True)],
        [sg.Button('Next Step')] 
    ]

    sg.Window(title, layout, keep_on_top=True, modal=True).read(close=2000)