import graphviz


class Tree:
    color_start = '#F96141'
    color_open = '#11BAFF'
    color_closed = '#FF6A0F'
    color_target = '#70FF1E'

    path_file = 'images/tree/'
    format_file = 'png'

    def __init__(self):
        # print('in constructor')
        self.u = graphviz.Digraph(self.path_file + 'asd', format=self.format_file,
                                  node_attr={'color': 'lightblue2', 'style': 'filled'})
        self.u.attr(size='6,6')
        self.edges = []
        # arreglo de imagenes
        self.filepaths = []
        # self.u = graphviz.Digraph()

    def set_name_file(self, filename):
        # self.u = graphviz.Digraph(self.path_file + filename, format='png',
        #                          node_attr={'color': 'lightblue2', 'style': 'filled'})
        self.u.filename = self.path_file + filename

    def set_node(self, name: str, type_text: str):
        if type_text == 'start':
            self.u.node(name, fillcolor=self.color_start)
        elif type_text == 'close':
            self.u.node(name, fillcolor=self.color_closed)
        elif type_text == 'target':
            self.u.node(name, fillcolor=self.color_target)
        else:
            self.u.node(name, fillcolor=self.color_open)

    def add_edge(self, start_node_name: str, end_node_name: str, cost: float):
        node_in_edges: Edge = next((x for x in self.edges if x.node_name == end_node_name), False)
        if node_in_edges is not False:
            node_in_edges.quantity += 1
            node_rename = end_node_name + '.' + str(node_in_edges.quantity)
            self.u.edge(start_node_name, node_rename, label=str(cost))
            edge = Edge(node_rename, start_node_name, end_node_name)
            self.edges.append(edge)
        else:
            edge = Edge(end_node_name, start_node_name, end_node_name)
            self.edges.append(edge)
            self.u.edge(start_node_name, end_node_name, label=str(cost))

    def add_edge_close(self, start_node_name: str, end_node_name: str, cost: float):
        node_in_edges: Edge = next((x for x in self.edges if x.node_name == end_node_name), False)
        # si ya existe agregarle su repeticion
        if node_in_edges is not False:
            node_in_edges.quantity += 1
            node_rename = end_node_name + '.' + str(node_in_edges.quantity)
            self.u.edge(start_node_name, node_rename, label=str(cost))
            self.set_node(node_rename, 'close')

    def close_others(self, end_node_name: str):
        # pintar como cerrado los demas nodos de ese nombre
        node_in_edges: Edge = next((x for x in self.edges if x.node_name == end_node_name), False)
        if node_in_edges is not False:
            for i in range(node_in_edges.quantity - 1):
                self.set_node(end_node_name + '.' + str(node_in_edges.quantity), 'close')
        # cerrar tambien el que no tiene .n siendo n un valor numerico
        self.set_node(end_node_name, 'close')
        # self.u.edge(start_node_name, end_node_name, label=str(cost))

    # def add_edge(self, start_node_name: str, end_node_name: str, cost: float):
    #     node_in_edges: Edge = next((x for x in self.edges if x.node_name == end_node_name), False)
    #     if node_in_edges is not False:
    #         node_in_edges.quantity += 1
    #         node_rename = end_node_name + '.' + str(node_in_edges.quantity)
    #         self.u.edge(start_node_name, node_rename, label=str(cost))

    def draw_example(self):
        self.set_node('A', 'start')
        self.set_node('B', '')
        self.set_node('C', 'close')
        self.set_node('D', 'target')

        self.add_edge('A', 'B', 4)
        self.add_edge('A', 'C', 6)
        self.add_edge('C', 'D', 2)

        self.u.view()

    def draw_tree(self, filename):
        self.set_name_file(filename)
        self.u.render(view=False)
        self.filepaths.append(self.path_file + filename + '.' + self.format_file)

    def add_end_node(self, node_name):
        end_node_edge = Edge(node_name)
        self.edges.append(end_node_edge)


class Edge:
    def __init__(self, node_name, start_node_name, end_node_orig):
        self.start_node_name = start_node_name
        self.node_name = node_name
        self.quantity = 1
        self.end_node_name_orig = end_node_orig


