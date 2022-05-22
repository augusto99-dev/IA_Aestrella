from ast import List
import random
from models.Graph import GraphPreview
from models.Node import Node
from models.Edge import Edge
# from views.Graph import Graph
from operator import attrgetter

from views.ShowResult import ShowResult
from views.Tree import Tree

import copy

import numpy as np


from views.show_tree_test import Step_to_step


class AStarController:
    open_nodes = []
    close_nodes = []
    short_path = []
    neighbors = []

    nodes = []
    edges = []

    current_node: Node = None
    start_node: Node = None
    end_node: Node = None

    path = []

    message_step = ''

    def __init__(self):
        # borra despues este
        # self.graph = Graph()
        # self.edge = Node()
        # self.node = Node()
        self.step = 0
        self.tree = Tree()
        self.graph_preview = GraphPreview()
        self.step_to_step_view = Step_to_step()
        self.view_showresult = ShowResult()
    def __repr__(self):
        return str(self.__dict__)

    def set_nodes(self,nodes_array):
        self.nodes = nodes_array

    def set_edges(self,edges_array):
        self.edges = edges_array
    
    def set_origin(self, origin):
        print('llega ... ', origin)
        self.start_node = self.get_node(origin)
        print('START : ', self.start_node)
    
    def set_final(self,final):
        print('llega final ... ', final)
        self.end_node = self.get_node(final)
        print('fin : ', self.end_node)
    

    def main(self):
        print('In main of Controller')

    def add_node(self, node_name: str, node_h: float):
        node = Node(node_name, 0, node_h, 0, None)
        self.graph_preview.add_node(node_name, node_name)
        self.nodes.append(node)

    def get_node(self, name: str) -> Node:
        # print('get node: ', self)
        node_enc = None
        for node in self.nodes:
            if node.name == name:
                node_enc = node
        return node_enc

    def add_edge(self, start, end, cost, di=True):
        # arista para parte grafica
        # self.graph.G.add_edge(start, end, weight=cost)
        # para el preview
        self.graph_preview.add_edge(start, end, cost)
        # Si el grafo no es dirigido
        # if not di:
            # Agrego otra arista en sentido contrario
            # self.graph.G.add_edge(end, start, weight=cost)
        # parte logica
        # obtengo el nodo para guardar sus aristas
        node = self.get_node(start)
        node.edges.append(Edge(node, self.get_node(end), cost))

    def add_neighbors(self):
        # pintar nodo actual como cerrado. Si no es el nodo inicial
        current_neighbors = self.current_node.get_neighbors()
        # print('neighbors del nodo actual ', current_neighbors)
        # arbol para mostrar solo vecinos del nodo actual
        for node in current_neighbors:
            node_in_close: Node = next((x for x in self.close_nodes if x.name == node.name), False)
            # si no esta en la lista de cerrados lo coloco
            if node_in_close is False:
                self.neighbors.append(node)

    def try_neighbors(self):
        current_node_text = ''
        neighbors_text = ''
        node_try_text = ''
        # si tiene vecinos lo marco como recorrido, sino no lo pinto
        if len(self.neighbors) > 0:
            self.paint_close_node(self.current_node.name)

        current_node_text = current_node_text + 'NODO ACTUAL: (' + self.current_node.name + ') \n'
        current_node_text = current_node_text + 'Se recorren sus vecinos: '
        for node in self.neighbors:
            print('VECINOS DEL NODO: ', self.current_node.name)
            print(node.name)
            neighbors_text = neighbors_text + node.name + ' ;'
            if any(x.name == node.name for x in self.open_nodes) is False and any(x.name == node.name for x in self.close_nodes) is False:
                copy_node = copy.copy(node)  # copia superficial
                self.open_nodes.append(copy_node)
                print('copiado a la lista de abiertos: ', node.name)
                # print('Copiado nodo vecino en la lista de abiertos')
                # self.tree.add_message_in_tree('Recorro los vecinos del nodo actual.')

                self.tree.add_edge(self.current_node.name, node.name, node.g)

            else:
                # verifico si esta en la lista de abiertos, si es asi retorno su valor. Sino retorna False
                node_in_open: Node = next((x for x in self.open_nodes if x.name == node.name), False)
                # print('por el else')
                # si ya se encuentra en la lista de abierto = is not none
                if node_in_open is not False:
                    # print('si no es none')
                    # print('node.g ', node.g)
                    # print('node_in_open.g ', node_in_open.g)
                    self.message_step = self.message_step + '\n El nodo ' + node_in_open.name + ' ya se encuenta en la lista de abiertos. '
                    if node.g < node_in_open.g:
                        # self.tree.add_edge(self.current_node.name, node.name, node.g)
                        # cierro los otros que estan abiertos
                        self.tree.close_others(node.name)
                        # coloco el nuevo que quedara abierto
                        # self.tree.add_message_in_tree(
                        #    'El nodo ya existe en otro lado pero este mejora a los demas abiertos \n '
                        #    'Por ello se recorre queda abierto y se cierran los otros')
                        node_try_text = node_try_text + '\n El nodo ' + node.name + ' mejora a los demas iguales abiertos \n '\
                                                                'Por ello se recorre queda abierto y se cierran los otros iguales. \n'
                        self.tree.add_edge(self.current_node.name, node.name, node.g)
                        # print('El g del nodo de vecino es menor al g del nodo de abierto')
                        # actualizo atributos del nodo de la lista de abierto con el de vecino

                        # print('antes de actualizar la lista de abiertos (deberia estar en cerrados este nodo luego )')
                        # print('\n ', node_in_open.name)
                        # print('\n con G=', node_in_open.g)
                        # node_in_open = node
                        node_in_open.g = node.g
                        node_in_open.h = node.h
                        node_in_open.f = node.f
                        node_in_open.predecessor = node.predecessor
                        print('actualizo LA LISTA DE ABIERTOS G.vec<G.abiet. ')
                        for node2 in self.neighbors:
                            print('\n ', node2.name)
                            print('\n ', node2.g)
                    else:
                        # aqui deberia pintar cerrado porque no mejora al que estaba en abiertos
                        # self.tree.add_message_in_tree('El nodo ya existe en otro lado pero no mejora al que ya estaba abierto \n '
                        #                              'Por ello se recorre pero queda cerrado')
                        node_try_text = node_try_text + '\n El nodo ' + node.name + ' no mejora a los demas iguales ya abiertos. ' \
                                                                                         'Es por ello que se cierra. \n'
                        self.tree.add_edge_close(self.current_node.name, node.name, node.g)
                        # self.tree.add_edge(self.current_node.name, node.name, node.g)
                else:
                        print('no esta en la lista de abiertos: ', node.name)

        self.step += 1
        self.tree.format_message_tree(current_node_text, neighbors_text, node_try_text)
        self.tree.draw_tree('step-' + str(self.step))
        self.message_step = ''

    # if any(x.name == "B" for x in self.open_nodes):
    #
    def calculate_attr(self):
        for node in self.neighbors:
            # print('cost test: ', self.current_node.get_cost(node))
            node.g = self.current_node.g + self.current_node.get_cost(node)
            # node.h = node.h # Ya tiene cargado el h desde el input
            node.f = float(node.g) + float(node.h)
            node.predecessor = self.current_node
            # print('Nodo in calculate_attr: ', node)

    def mov_promising_node_from_open_to_closed(self):
        ob_min = min(self.open_nodes, key=attrgetter('f'))
        # print('objeto mas bajo: ', ob_min)
        print(' \n EL MAS PROMETEDOR: ', ob_min.name)
        print('\n CON F: ', ob_min.f)
        print('\n CON G: ', ob_min.g)
        self.open_nodes.remove(ob_min)
        self.close_nodes.append(ob_min)
        # print('lista de abiertos despues de eliminar: ', self.open_nodes)
        # print('lista de cerrados despues de agregar: ', self.close_nodes)

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


    def draw_start_node(self):
        self.step += 1
        self.tree.add_message_in_tree('Nodo inicial indicado por el usuario.')
        self.tree.set_node(self.start_node.name, 'start')
        self.tree.draw_tree('step-' + str(self.step))

    def paint_close_node(self, node_name: str):
        self.tree.set_node(node_name, 'close')

    def paint_target_node(self):
        self.tree.set_node(self.end_node.name, 'target')
        self.tree.add_message_in_tree('El nodo ' + self.end_node.name + ' es el mas prometedor y '
                                                                        'objetivo. Fin del proceso')
        self.tree.draw_tree('step-' + str(self.step))

    def launch_window_step(self):
        cont = 0
        # for filepath in self.tree.filepaths:
        print('filepaths: ', self.tree.filepaths)
        print('filepath size ', len(self.tree.filepaths))
        while cont < len(self.tree.filepaths):
            action = self.step_to_step_view.steptostep(cont, self.tree.filepaths[cont], 'message', 50, 50)
            print('retorno: ', action)
            if action == 'back':
                cont -= 1
            elif action == 'exit':
                break
            elif action == 'next':
                cont += 1

    def launch_window_direct_result(self):
        img_path = self.get_path_last_step()
        self.view_showresult.showresult("Resultado Directo", img_path, "")

    def draw_graph_preview(self):
        self.graph_preview.draw_example()

    def getPreviewPath(self):
        self.graph_preview.draw_preview()
        return self.graph_preview.directory

    def get_path_last_step(self):
        self.run_alghoritm()
        last_path = self.tree.filepaths[-1]
        return last_path

    def run_alghoritm(self):
        # tree: Tree = Tree('start')
        self.tree = Tree()
        # estos se deberian setear en la vista:
        print('ALG START: ', self.start_node)
        print('ALG END ', self.end_node)
        # self.start_node = self.nodes[0]
        # self.end_node = self.nodes[-1]

        # variable para indicar que no se encontro el camino
        exist_path = True

        self.close_nodes.append(self.start_node)
        cont = 0
        # pintar nodo inicial

        # draw tree
        self.draw_start_node()
        while next((x for x in self.close_nodes if x.name == self.end_node.name), False) is False:
            asd = next((x for x in self.close_nodes if x.name == self.end_node.name), False)
            # obtengo el ultimo elemento de la lista de cerrados.
            self.current_node = self.close_nodes.pop()
            # el anterior lo quita, entonces lo vuelvo a poner
            self.close_nodes.append(self.current_node)
            self.add_neighbors()
            # pintar vecinos
            # if exit_draw is False:
            # print('----- VECINOS A PINTAR --------', controller.neighbors)
            # for node in controller.neighbors:
            # exit_draw = True
            self.calculate_attr()
            self.try_neighbors()
            self.neighbors.clear()
            if len(self.open_nodes) == 0:
                print('El nodo inicial y final no se encuentran relacionados!!')
                exist_path = False
                break
            self.mov_promising_node_from_open_to_closed()
            cont += 1
        if exist_path is True:
            # pintar nodo objetivo
            self.paint_target_node()
            # RUTA CORTA:
            self.get_path()
        else:
            # creo un paso mas indicando que no existe un camino hacia el destino.
            self.paint_not_exist_path()
        # reinicio para lo ultimo
        self.neighbors = []
        self.open_nodes = []
        self.close_nodes = []
        self.neighbors = []
        # ver filepaths
        # print('Filepaths: ', controller.tree.filepaths)
        # controller.launch_window_step()

    def paint_not_exist_path(self):
        self.step += 1
        self.tree.add_message_in_tree('El nodo final: ' + self.end_node.name + ' Es inalcanzable!')
        self.tree.draw_tree('step-' + str(self.step))
        self.message_step = ''

# if __name__ == '__main__':
#     aStar = AStarController()
#     aStar.main()

# def get_node_in_list(self):,

# Funcion de carga de nodo de forma aleatoria
    def random_nodes(self,cant)-> List:
        # verifico si ya esta cargado algun nodo en el controlador
        if len(self.nodes) > 0:
            return False
        #Lista de nombres posibles de nodos
        name_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T']
        #Crea una lista de 15 nombres aleatorios a partir de la lista de nombres
        elec_list = random.sample(name_list, int(cant))
        nodo = []
        node_list= []
        #Por cada nombre en la lista cre el objeto nodo y devuelve la lista a la vista
        for i in elec_list:
            #Heuritica aleatoria entre 1 y 60
            heurist = random.randint(1, 60)
            nodo.append(i)
            nodo.append(heurist)
            self.add_node(i,heurist)
            node_list.append(nodo)
            nodo = []
        # set nodos finales e iniciales, primero y ultimo si ya son aleatorios
        self.start_node = self.nodes[0]
        self.end_node = self.nodes[-1]
        return node_list
    
    # def random_edges(self) -> List:
    #     elect_start = random.choice(self.nodes, 15)
    #     elect_final = random.choice(self.nodes, 15)
    #     print(elect_start)
    #     edge = []
    #     edge_list = []
    #     for i in range(15):
    #         cost = random.randint(1, 60)
    #         edge.append(elect_start[i].name)
    #         edge.append(elect_final[i].name)
    #         edge.append(cost)
    #         self.add_edge(elect_start[i].name,elect_final[i].name,cost)
    #         edge_list.append(edge)
    #         edge = []
    #     return edge_list

    # def random_edges(self) -> List:
    #     edge = []
    #     edge_list = []
    #     for i in range(15):
    #         cost = random.randint(1, 60)
    #         node_start = self.nodes[random.randint(0, len(self.nodes) -1)]
    #         node_end = self.nodes[random.randint(0, len(self.nodes) -1)]
    #         print('NODO RANDOM START: ', node_start)
    #         print('NODO RANDOM END: ', node_end)
    #         print('cost : ', cost)
    #         self.add_edge(node_start.name, node_end.name, cost)
    #         edge.append(node_start.name)
    #         edge.append(node_end.name)
    #         edge_list.append(edge)
    #         edge = []
    #     return edge_list

    def random_edges(self,cant) -> List:
        fisrt_rand = True
        # verifico si ya no se cargo al controlador (Para que no se carguen de nuevo)
        if len(self.nodes[0].edges) > 0:
            return False
        # recibo la cantidad de relaciones por parametro
        relationship_quantity = int(cant)
        edge = []
        edge_list = []

        nodes_quantity = len(self.nodes)
        relationship_quantity_control = relationship_quantity+2

        for node in self.nodes:
            # si ya se terminaron las cantidades de relaciones skipeo
            if relationship_quantity_control <= 0:
                break

            relation_ship_control_node = int(np.random.uniform(0, relationship_quantity_control) / 2)
                # random.randint(0, relationship_quantity_control)
            print('nodo : ', node.name)
            print('cantidad de relaciones rand: ', relation_ship_control_node)
            # se descontaran las cantidades para mantener el total cargado
            relationship_quantity_control -= relation_ship_control_node
            # relacionar ese nodo con otros nodos. (la cantidad especificada arriba)
            cont = 0
            flag = False
            aux_exit_iterator = 0
            while cont < relation_ship_control_node and flag is False:
                print('en while. ', cont)
                # aca se arman las relaciones
                cost = random.randint(1, 60)
                node_end = self.nodes[random.randint(0, nodes_quantity - 1)]
                # verifico no relacionar al mismo nodo
                if node_end.name != node.name:
                    # verifico no repetir la relacion
                    if cont >= nodes_quantity - 1:
                        flag = True
                    if node_end not in node.get_neighbors():
                        self.add_edge(node.name, node_end.name, cost)
                        edge.append(node.name)
                        edge.append(node_end.name)
                        edge_list.append(edge)
                        edge = []
                        cont += 1




        # for i in range(15):
        #     cost = random.randint(1, 60)
        #     node_start = self.nodes[random.randint(0, len(self.nodes) -1)]
        #     node_end = self.nodes[random.randint(0, len(self.nodes) -1)]
        #     print('NODO RANDOM START: ', node_start)
        #     print('NODO RANDOM END: ', node_end)
        #     print('cost : ', cost)
        #     self.add_edge(node_start.name, node_end.name, cost)
        #     edge.append(node_start.name)
        #     edge.append(node_end.name)
        #     edge_list.append(edge)
        #     edge = []
        return edge_list