import matplotlib.pyplot as plt
import networkx as nx

class qTree():
    def __init__(self):
        self.root_node = None
        self.nodes = {}

    def add_node(self, child_node, parent_node = None):
        self.nodes[child_node] = child_node

        if parent_node is not None:
            self.nodes[parent_node].children.append(child_node)
        else:
            self.root_node = child_node

        return child_node

    def get_node(self, identifier):
        return self.nodes.get(identifier, None)

    def is_leaf(self, identifier):
        return identifier in self.nodes and not self.nodes[identifier].children

    def all_nodes(self):
        return self.nodes.values()

    def print_tree(self, node, level=0):
        print('  ' * level + str(node))
        for child in node.children:
            self.print_tree(child, level + 1)

    def draw_tree(self):
        G = nx.DiGraph()
        for node in self.all_nodes():
            G.add_node(str(node.get_value()))
            for child in node.children:
                G.add_edge(str(node.get_value), str(child.get_value()))

        nx.draw(G, with_labels=True)
        plt.show()

    def get_root(self):
        return self.nodes[self.root_node]

    def existing_node(self, node):
        for existing_node in self.nodes.values():
            if existing_node.get_current_states() == node.get_current_states():
                return True
        return False
