# from models.Edge import Edge


class Node:
    edges = []

    def __init__(self, name, g, h, f, predecessor):
        self.name = name
        self.g: float = g
        self.f: float = f
        self.h: float = h
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

    def get_cost(self, node) -> float:
        # busco la arista que el inicial sea el propio nodo y el final sea el nodo del parametro.
        node_search = next((x for x in self.edges if x.start.name == self.name and x.end.name == node.name), False)
        print('node Search: ', node_search)
        return float(node_search.cost)
