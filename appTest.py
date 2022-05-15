from models.Node import Node
from controllers.AStarController import AStarController
from models.Test import Test

if __name__ == '__main__':
    controller = AStarController()
    test = Test(controller)
    test.run_test(controller)


