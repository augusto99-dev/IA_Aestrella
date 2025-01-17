from models.Node import Node
from models.Edge import Edge
from views.Graph import Graph
from operator import attrgetter

import copy


class AStarController:
    open_nodes = []
    close_nodes = []
    short_path = []
    neighbors = []

    nodes = []

    current_node: Node = None
    start_node: Node = None
    end_node: Node = None

    path = []

    def __init__(self):
        self.graph = Graph()
        # self.edge = Node()
        # self.node = Node()

    def __repr__(self):
        return str(self.__dict__)

    def main(self):
        print('In main of Controller')

    def get_node(self, name: str) -> Node:
        print('get node: ', self)
        node_enc = None
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

    def add_neighbors(self):
        current_neighbors = self.current_node.get_neighbors()
        print('neighbors del nodo actual ', current_neighbors)
        for node in current_neighbors:
            if node not in self.close_nodes:
                print('no esta en la lista de cerrados, ', node)
                self.neighbors.append(node)

    def try_neighbors(self):
        for node in self.neighbors:
            if any(x.name == node.name for x in self.open_nodes) is False and node not in self.close_nodes:
                copy_node = copy.copy(node)  # copia superficial
                self.open_nodes.append(copy_node)
                print('Copiado nodo vecino en la lista de abiertos')
            else:
                # verifico si esta en la lista de abiertos, si es asi retorno su valor. Sino retorna False
                node_in_open: Node = next((x for x in self.open_nodes if x.name == node.name), False)
                # print('por el else')
                # si ya se encuentra en la lista de abierto = is not none
                if node_in_open is not False:
                    # print('si no es none')
                    # print('node.g ', node.g)
                    # print('node_in_open.g ', node_in_open.g)
                    if node.g < node_in_open.g:
                        print('El g del nodo de vecino es menor al g del nodo de abierto')
                        # actualizo atributos del nodo de la lista de abierto con el de vecino
                        node_in_open.g = node.g
                        node_in_open.h = node.h
                        node_in_open.f = node.f
                        node_in_open.predecessor = node.predecessor

    # if any(x.name == "B" for x in self.open_nodes):
    #
    def calculate_attr(self):
        for node in self.neighbors:
            print('cost test: ', self.current_node.get_cost(node))
            node.g = self.current_node.g + self.current_node.get_cost(node)
            # node.h = node.h # Ya tiene cargado el h desde el input
            node.f = float(node.g) + float(node.h)
            node.predecessor = self.current_node
            print('Nodo in calculate_attr: ', node)

    def mov_promising_node_from_open_to_closed(self):
        ob_min = min(self.open_nodes, key=attrgetter('f'))
        print('objeto mas bajo: ', ob_min)
        self.open_nodes.remove(ob_min)
        self.close_nodes.append(ob_min)
        print('lista de abiertos despues de eliminar: ', self.open_nodes)
        print('lista de cerrados despues de agregar: ', self.close_nodes)

    def get_path(self):
        target_node: Node = self.close_nodes.pop()
        aux_pred: Node = target_node.predecessor
        self.path.append(target_node)
        while aux_pred is not None:
            self.path.append(aux_pred)
            aux_pred = aux_pred.predecessor
        print('CAMINO: ')
        for node in self.path:
            print('\n -- : ', node.name)

    def drawGraphs(self):
        self.graph.draw("TRABAJO PRACTICO FINAL IA 1")

# if __name__ == '__main__':
#     aStar = AStarController()
#     aStar.main()

# def get_node_in_list(self):
