from controllers.AStarController import AStarController
from examples.Test import Test

if __name__ == '__main__':
    controller = AStarController()
    test = Test(controller)
    test.run_test(controller)


