from models.Node import Node


class Edge:
    end: Node

    def __init__(self, start, end: Node, cost):
        self.start = start
        self.end = end
        self.cost = cost
