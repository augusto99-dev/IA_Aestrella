import graphviz


class Tree:
    color_start = '#F96141'
    color_open = '#11BAFF'
    color_closed = '#FF6A0F'
    color_target = '#70FF1E'

    def __init__(self):
        print('in constructor')
        self.u = graphviz.Digraph('unix', format='png',
                                  node_attr={'color': 'lightblue2', 'style': 'filled'})
        self.u.attr(size='6,6')
        self.edges_view = []

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

    def draw_tree(self):
        self.u.view()

