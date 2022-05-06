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
