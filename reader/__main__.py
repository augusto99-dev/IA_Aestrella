from controllers.AStarController import AStarController
from examples.Test import Test


def main():
    controller = AStarController()
    test = Test(controller)
    test.run_test(controller)