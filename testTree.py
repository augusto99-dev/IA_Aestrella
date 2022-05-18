from controllers.AStarController import AStarController
from views.Tree import Tree
from models.Test_step_step2 import Test
from views.ViewPrincipal import ViewPrincipal

if __name__ == '__main__':
    # tree = Tree()
    # tree.draw_example()
    controller = AStarController()
    main_win = ViewPrincipal(controller)
    main_win.launch_view()
    # test = Test(controller)
    # test.run_test(controller)
