from models.Node import Node
from views.Graph import Graph


class AStarController:
    open_nodes = []
    close_nodes = []
    short_path = []
    neighbors = []

    nodes = []
    edges = []

    current_node = None
    start_node = None
    end_node = None

    def __init__(self):
        self.graph = Graph()
        # self.edge = Node()
        # self.node = Node()

    def main(self):
        print('In main of Controller')

    def get_node(self, name):
        for node in self.nodes:
            if node.name == name:
                node_enc = node
        return node_enc

    def add_edge(self, u, v, w=1, di=True):
        self.graph.G.add_edge(u, v, weight=w)

        # Si el grafo no es dirigido
        if not di:
            # Agrego otra arista en sentido contrario
            self.graph.G.add_edge(v, u, weight=w)

    def drawGraphs(self):
        self.graph.draw("TRABAJO PRACTICO FINAL IA 1")

# if __name__ == '__main__':
#     aStar = AStarController()
#     aStar.main()