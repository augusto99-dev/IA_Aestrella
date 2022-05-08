class Node:
    edges = []

    def __init__(self, name, g, h, f, predecessor):
        self.name = name
        self.g = g
        self.f = f
        self.h = h
        self.predecessor = predecessor

    def __repr__(self):
        return str(self.__dict__)

    def to_string_edges(self):
        for edge in self.edges:
            # print('Nodo actual ', edge.start.name)
            print('Uno de sus vecinos es: ', edge.end.name)
            print('Costo asociado ', edge.cost)

    def get_neighbors(self):
        neighbors_ret = []
        for edge in self.edges:
            neighbors_ret.append(edge.end)
        return neighbors_ret
