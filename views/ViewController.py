import os
from controllers.AStarController import AStarController
from views.Desktop_Floating_Toolbar_Examples import ExamplesController
from views.ViewPrincipal import ViewPrincipal
import PySimpleGUI as sg
import webbrowser


class ViewController:
    def __init__(self):
        self.controller = AStarController()


    def launch_main_win(self):
        # limpiamos valores de una prueba vieja
        self.controller.reset_values()
        view_main = ViewPrincipal(self.controller)
        view_main.launch_view()

    def print_docs(self):
        print('LANZAR DOCUMENTO PDF')
        # path = 'docs/informe.pdf'
        path2 = os.path.join(os.getcwd(), 'docs/informe.pdf')
        webbrowser.open_new(path2)

    def launch_examples_view(self):
        print('Lanzando vista de ejemplos')
        view_examples = ExamplesController()
        view_examples.launch_examples_view()

    def launch_guide(self):
        print('Lanzando vista de ejemplos')
        path_guide = os.path.join(os.getcwd(), 'docs/guia-rapida.pdf')
        webbrowser.open_new(path_guide)

    def launch_repo(self):
        print('repo de github')
        url = "https://github.com/augusto99-dev/IA_Aestrella/"
        webbrowser.open_new(url)

    def get_credits(self):
        versions = "IMPLEMENTACIÓN DE ALGORITMO 'A ESTRELLA' \n \n Version de la APP: {}.{}.{}\nIntegrantes: \n - {}\n - {}\n - {}\n \n \n Ingeniería en Informatica - Universidad Gaston Dachary".format(
            '1', '0', '0', 'Augusto Noguera', 'Julio Alves', 'Carolina Ruiz')
        return versions

    def launch_view_credits(self):
        sg.popup_scrolled(self.get_credits())