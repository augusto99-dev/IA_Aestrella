from models.Node import Node
from models.Edge import Edge
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

    def get_node(self, name: str) -> Node:
        for node in self.nodes:
            if node.name == name:
                node_enc = node
        return node_enc

    def add_edge(self, start, end, cost, di=True):
        # arista para parte grafica
        self.graph.G.add_edge(start, end, weight=cost)
        # Si el grafo no es dirigido
        if not di:
            # Agrego otra arista en sentido contrario
            self.graph.G.add_edge(end, start, weight=cost)
        # parte logica
        # obtengo el nodo para guardar sus aristas
        node = self.get_node(start)
        node.edges.append(Edge(node, self.get_node(end), cost))

    def drawGraphs(self):
        print('aristas de A')
        self.get_node("A").to_string_edges()
        self.graph.draw("TRABAJO PRACTICO FINAL IA 1")



# if __name__ == '__main__':
#     aStar = AStarController()
#     aStar.main()