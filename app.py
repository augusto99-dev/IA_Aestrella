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

            controller.nodes.append(Node(name, 0, h, 0, None))
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
            # node = controller.get_node(start)
            # print('nodo del get: ', node)
            # end_node = controller.get_node(end)
            # print('nodo del get END: ', end_node)
            # node.edges.append(Edge(node, end_node, cost))
            # print('edges del nodo. ', node.edges)
    except KeyboardInterrupt:
        pass
    for n in controller.nodes:
        print(n.name)

    controller.start_node = controller.get_node(input('NODO INICIAL '))
    controller.end_node = controller.get_node(input('NODO FINAL '))

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

    # TEST calculate_attr (con ABC del primer ejemplo realizado)
    # controller.current_node = controller.nodes[0]
    # controller.neighbors.append(controller.nodes[1])
    # controller.neighbors.append(controller.nodes[2])
    # print('neighbors antes del calculate_attr: ', controller.neighbors)
    # print('Nodo actual: ', controller.nodes[0])
    # controller.calculate_attr()
    # print('neighbors despues del calculate_attr: ', controller.neighbors)

    # TEST mov_promising_node_from_open_to_closed (me prendo del anterior para probar, descomentar anterior y probar)
    # controller.open_nodes = controller.neighbors
    # controller.mov_promising_node_from_open_to_closed()

    # main process star
    controller.close_nodes.append(controller.start_node)
    cont = 0
    print('test de vecinos: ')
    print('NODE 0', controller.nodes[0].edges)
    print('\n -----')
    print('NODE 1', controller.nodes[1].edges)
    print('\n -----')
    print('NODE 2', controller.nodes[2].edges)

    print('Vecinos inicialmente de c1. ', controller.nodes[2].edges)

    while next((x for x in controller.close_nodes if x.name == controller.end_node.name), False) is False:
        asd = next((x for x in controller.close_nodes if x.name == controller.end_node.name), False)
        print('resultado de comparar si es el ultimo: ', asd)
        print('iteracion::: ', cont)
        print('LISTA DE CERRADOS ANTES DE OBTENER EL ULTIMO: ', controller.close_nodes)
        # obtengo el ultimo elemento de la lista de cerrados.
        controller.current_node = controller.close_nodes.pop()
        print('NODO ACTUALL OBTENIDO DE LA LISTA DE CERRADOS: ', controller.current_node)
        print('aristas del nodo actual: ', controller.current_node.get_neighbors())
        # el anterior lo quita, entonces lo vuelvo a poner
        controller.close_nodes.append(controller.current_node)
        controller.add_neighbors()
        print('neigbors antes de calculate attr:: ', controller.neighbors)
        controller.calculate_attr()
        controller.try_neighbors()
        controller.neighbors.clear()
        controller.mov_promising_node_from_open_to_closed()

        print('open nodes: ', controller.open_nodes)
        print('closed nodes: ', controller.close_nodes)

        print('nodo final. ', controller.end_node)
        cont += 1

    # RUTA CORTA:
    controller.get_path()


    # controller.drawGraphs()

