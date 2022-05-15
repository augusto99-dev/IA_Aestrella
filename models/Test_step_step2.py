from controllers.AStarController import AStarController
from models.Node import Node

from views.Tree import Tree


class Test:
    def __init__(self, controller: AStarController):
        # carga de nodos (Problema de clase)
        node_a = Node('A', 0, 58, 0, None)
        controller.nodes.append(node_a)
        node_b = Node('B', 0, 30, 0, None)
        controller.nodes.append(node_b)
        node_c = Node('C', 0, 78, 0, None)
        controller.nodes.append(node_c)
        node_d = Node('D', 0, 20, 0, None)
        controller.nodes.append(node_d)
        node_e = Node('E', 0, 25, 0, None)
        controller.nodes.append(node_e)
        node_f = Node('F', 0, 10, 0, None)
        controller.nodes.append(node_f)
        node_g = Node('G', 0, 20, 0, None)
        controller.nodes.append(node_g)
        node_h = Node('H', 0, 20, 0, None)
        controller.nodes.append(node_h)
        node_i = Node('I', 0, 80, 0, None)
        controller.nodes.append(node_i)
        node_j = Node('J', 0, 20, 0, None)
        controller.nodes.append(node_j)
        node_k = Node('K', 0, 0, 0, None)
        controller.nodes.append(node_k)
        # nodo inicial y final
        controller.start_node = node_a
        controller.end_node = node_k

        # relaciones
        controller.add_edge("A", "B", 90)
        controller.add_edge("A", "C", 70)
        controller.add_edge("A", "D", 20)
        controller.add_edge("A", "E", 15)
        controller.add_edge("B", "C", 10)
        controller.add_edge("B", "F", 30)
        controller.add_edge("B", "I", 40)
        controller.add_edge("C", "B", 10)
        controller.add_edge("C", "A", 70)
        # controller.add_edge("C", "G", 32)
        controller.add_edge("D", "H", 20)
        controller.add_edge("H", "E", 60)
        controller.add_edge("E", "G", 15)
        controller.add_edge("G", "C", 32)
        controller.add_edge("I", "J", 35)
        controller.add_edge("F", "K", 15)
        controller.add_edge("J", "K", 30)

    def run_test(self, controller: AStarController):
        # tree: Tree = Tree('start')
        controller.close_nodes.append(controller.start_node)
        cont = 0
        # pintar nodo inicial

        # draw tree
        controller.draw_start_node()
        while next((x for x in controller.close_nodes if x.name == controller.end_node.name), False) is False:
            asd = next((x for x in controller.close_nodes if x.name == controller.end_node.name), False)
            # obtengo el ultimo elemento de la lista de cerrados.
            controller.current_node = controller.close_nodes.pop()
            # el anterior lo quita, entonces lo vuelvo a poner
            controller.close_nodes.append(controller.current_node)
            controller.add_neighbors()
            # pintar vecinos
            # if exit_draw is False:
            # print('----- VECINOS A PINTAR --------', controller.neighbors)
            # for node in controller.neighbors:
            # exit_draw = True
            controller.calculate_attr()
            controller.try_neighbors()
            controller.neighbors.clear()
            controller.mov_promising_node_from_open_to_closed()
            cont += 1
        # pintar nodo objetivo
        controller.paint_target_node()

        # RUTA CORTA:
        controller.get_path()

        # ver filepaths
        print('Filepaths: ', controller.tree.filepaths)



