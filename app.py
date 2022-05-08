from calendar import c
# import networkx as nx
# import matplotlib.pyplot as plt
from models.Node import Node
from models.Edge import Edge
from controllers.AStarController import AStarController
# from tkinter import *

import copy  # modulo para hacer copias superficiales y profundas


# nodes = []
# edges = []

# https://networkx.org/documentation/stable/reference/classes/generated/networkx.DiGraph.add_edge.html?highlight=add_edge#networkx.DiGraph.add_edge
# Note: The nodes u and v will be automatically added if they are not already in the graph.

if __name__ == '__main__':

    controller = AStarController()

    controller.main()
    """     add_edge(G, "A", "B", 5)
    add_edge(G, "A", "D", 4)
    add_edge(G, "A", "E", 2)
    add_edge(G, "B", "C", 1, False)
    add_edge(G, "B", "E")
    add_edge(G, "C", "D", 3, False)
    add_edge(G, "C", "F", 5)
    add_edge(G, "D", "E", 3)
    add_edge(G, "D", "F", 4)
    add_edge(G, "E", "F", 8) """

    print("Ingrese Valores de los nodos \nCtrl + C PARA SALIR")
    cont = 1
    try:
        while True:
            name = input('Ingrese Nombre del Node ' + str(cont) + ': ')
            h = input('Ingrese el valor de h ' + str(cont) + ': ')
            cont += 1

            controller.nodes.append(Node(name, None, h, None, None))
    except KeyboardInterrupt:
        pass
    contEdges = 1
    print("Ingrese Valores de las aristas \nCtrl + C PARA SALIR")
    try:
        while True:
            start = input('Ingrese Node Inicial arista ' + str(contEdges) + ': ')
            end = input('Ingrese Node Final arista ' + str(contEdges) + ': ')
            cost = input('Ingrese cost del Node arista ' + str(contEdges) + ': ')
            contEdges += 1
            controller.add_edge(start, end, cost)
    except KeyboardInterrupt:
        pass
    for n in controller.nodes:
        print(n.name)
    # for a in controller.edges:
    #     print(a.start.name)

    # TEST para el metodo de obtener vecinos
    # controller.neighbors = controller.get_node("A").get_neighbors()
    # print('vecinos del controlador: ', controller.neighbors)

    # TEST de add vecinos
    # controller.current_node = controller.nodes[0]
    # controller.close_nodes.append(controller.nodes[2])
    # controller.add_neighbors()
    # print('Nodo actual: ', controller.nodes[0])
    # print('lista de cerrados: ', controller.close_nodes)
    # print('Lista de vecinos: ', controller.neighbors)

    # TEST de tratar vecinos
    # controller.close_nodes.append(controller.nodes[0])  # A
    # neig_b: Node = controller.nodes[1]
    # neig_b.g = 3
    # controller.neighbors.append(neig_b)  # B
    # neig_c: Node = controller.nodes[2]
    # neig_c.g = 5
    # controller.neighbors.append(neig_c)  # C
    #
    # open_b: Node = controller.nodes[1]  # B
    # copy_open_b = copy.copy(open_b)
    # copy_open_b.g = 4
    # controller.open_nodes.append(copy_open_b)  # B
    # controller.try_neighbors()
    # print('neighbors list: ', controller.neighbors)
    # print('open list: ', controller.open_nodes)

    controller.drawGraphs()

