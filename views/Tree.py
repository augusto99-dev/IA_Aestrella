import graphviz


class Tree:
    color_start = '#F96141'
    color_open = '#11BAFF'
    color_closed = '#FF6A0F'
    color_target = '#70FF1E'

    path_file = 'images/tree/'

    def __init__(self):
        print('in constructor')
        self.u = graphviz.Digraph(self.path_file + 'asd', format='png',
                                  node_attr={'color': 'lightblue2', 'style': 'filled'})
        self.u.attr(size='6,6')
        self.edges = []
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
        else:
            edge = Edge(end_node_name)
            self.edges.append(edge)
            self.u.edge(start_node_name, end_node_name, label=str(cost))

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
        self.u.view()

    def add_end_node(self, node_name):
        end_node_edge = Edge(node_name)
        self.edges.append(end_node_edge)


class Edge:
    def __init__(self, node_name):
        self.node_name = node_name
        self.quantity = 1


