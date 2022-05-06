class Node:
    def __init__(self, name, g, h, f, predecessor):
        self.name = name
        self.g = g
        self.f = f
        self.h = h
        self.predecessor = predecessor
