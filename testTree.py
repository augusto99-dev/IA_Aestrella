from controllers.AStarController import AStarController
from views.Tree import Tree
from models.Test_step_step2 import Test

if __name__ == '__main__':
    # tree = Tree()
    # tree.draw_example()
    controller = AStarController()
    test = Test(controller)
    test.run_test(controller)
