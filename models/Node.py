class Node:
    edges = []

    def __init__(self, name, g, h, f, predecessor):
        self.name = name
        self.g = g
        self.f = f
        self.h = h
        self.predecessor = predecessor

    def to_string_edges(self):
        for edge in self.edges:
            print('end ', edge.end.name)
            print('cost ', edge.end.name)
