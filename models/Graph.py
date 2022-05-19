import graphviz


class GraphPreview:
    color_start = '#F96141'
    color_open = '#11BAFF'
    color_closed = '#FF6A0F'
    color_target = '#70FF1E'

    path_file = 'images/graph/preview/'
    format_file = 'png'
    filename = 'preview-graph'

    def __init__(self):
        # print('in constructor')
        # self.u = graphviz.Digraph(self.path_file + 'asd', format=self.format_file,
        #                          node_attr={'color': 'lightblue2', 'style': 'filled'})
        self.u = graphviz.Graph('G', filename= self.filename + '.' + self.format_file, engine='sfdp', format=self.format_file, directory=self.path_file)
        self.u.attr(size='6,6')
        self.directory = self.path_file + self.filename + '.' + self.format_file

    def draw_example(self):
        self.add_node('A', 'A')
        self.add_node('B', 'B')
        self.add_node('C', 'C')
        self.add_node('D', 'D')
        self.add_node('E', 'E')
        self.add_edge('A', 'B', 2)
        self.add_edge('A', 'C', 3)
        self.add_edge('C', 'D', 4)
        self.add_edge('D', 'B', 4)
        self.add_edge('C', 'D', 4)
        self.add_edge('B', 'E', 4)
        self.add_edge('A', 'E', 4)
        self.u.render(view=True)

    def draw_preview(self):
        self.u.render(view=False)

    def add_edge(self, start_node_name: str, end_node_name: str, cost: float):
        self.u.edge(start_node_name, end_node_name, weight=str(cost))

    def add_node(self, key_node: str, node_name: str):
        self.u.node(key_node, node_name)
