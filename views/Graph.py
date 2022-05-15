import networkx as nx
import matplotlib.pyplot as plt


class Graph:

    def __init__(self):
        self.G = nx.DiGraph()

    def main(self):
        print('In main of View')

    def draw(self, title):
        # Draw the networks -- Meter en una funcion, preferentemente en otro archivo de vista
        pos = nx.layout.planar_layout(self.G)
        nx.draw_networkx(self.G, pos)
        labels = nx.get_edge_attributes(self.G, 'weight')
        nx.draw_networkx_edge_labels(self, pos, edge_labels=labels)
        plt.title(title)
        plt.show()


def draw_example(self):
    tree = ete3.Tree()
    for parent, children in itertools.groupby(graph.edges(), lambda edge:edge[0]):
        subtree = ete3.Tree(name=parent)
        for child in children:
            subtree.add_child(name=child[1])
            tree.add_child(child=subtree, name=parent)
    print(tree) 


    # Graph
    edges = [('lvl-1', 'lvl-2.1'), ('lvl-1', 'lvl-2.2'), ('lvl-2.1', 'lvl-3.1'), ('lvl-2.1', 2), ('lvl-2.2', 4),
         ('lvl-2.2', 6), ('lvl-3.1', 'lvl-4.1'), ('lvl-3.1', 5), ('lvl-4.1', 1), ('lvl-4.1', 3), ('input', 'lvl-1')]    
    G = nx.OrderedDiGraph()
    G.add_edges_from(edges)

    # Tree
    root = "input"
    subtrees = {node: ete3.Tree(name=node) for node in G.nodes()}
    [*map(lambda edge:subtrees[edge[0]].add_child(subtrees[edge[1]]), G.edges())]
    tree = subtrees[root]
    print(tree.get_ascii())
