import os

from controllers.AStarController import AStarController
from views.Desktop_Floating_Toolbar_Examples import ExamplesController
from views.ViewPrincipal import ViewPrincipal
import sys
import webbrowser


class ViewController:
    def __init__(self):
        self.controller = AStarController()


    def launch_main_win(self):
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

    def launch_repo(self):
        print('repo de github')
