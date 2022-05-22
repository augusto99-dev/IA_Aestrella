from controllers.AStarController import AStarController
from models.Node import Node


class Test:
    def __init__(self, controller: AStarController):
        # carga de nodos (Problema resuelto en carpeta)
        node_a = Node('A', 0, 14, 0, None)
        controller.nodes.append(node_a)
        node_b = Node('B', 0, 12, 0, None)
        controller.nodes.append(node_b)
        node_c = Node('C', 0, 11, 0, None)
        controller.nodes.append(node_c)
        node_d = Node('D', 0, 6, 0, None)
        controller.nodes.append(node_d)
        node_e = Node('E', 0, 4, 0, None)
        controller.nodes.append(node_e)
        node_f = Node('F', 0, 11, 0, None)
        controller.nodes.append(node_f)
        node_z = Node('Z', 0, 0, 0, None)
        controller.nodes.append(node_z)

        # nodo inicial y final
        controller.start_node = node_a
        controller.end_node = node_z

        # relaciones
        controller.add_edge("A", "B", 4)
        controller.add_edge("A", "C", 3)
        controller.add_edge("B", "F", 5)
        controller.add_edge("B", "E", 12)
        controller.add_edge("C", "D", 7)
        controller.add_edge("C", "E", 10)
        controller.add_edge("D", "E", 2)
        controller.add_edge("E", "Z", 5)

    def run_test(self, controller: AStarController):
        controller.close_nodes.append(controller.start_node)
        cont = 0
        while next((x for x in controller.close_nodes if x.name == controller.end_node.name), False) is False:
            asd = next((x for x in controller.close_nodes if x.name == controller.end_node.name), False)
            # obtengo el ultimo elemento de la lista de cerrados.
            controller.current_node = controller.close_nodes.pop()
            # el anterior lo quita, entonces lo vuelvo a poner
            controller.close_nodes.append(controller.current_node)
            controller.add_neighbors()
            controller.calculate_attr()
            controller.try_neighbors()
            controller.neighbors.clear()
            controller.mov_promising_node_from_open_to_closed()
            cont += 1
        # RUTA CORTA:
        controller.get_path()
        # controller.graph.draw("Ruta Corta")

        # ver filepaths
        print('Filepaths: ', controller.tree.filepaths)
        controller.launch_window_step()