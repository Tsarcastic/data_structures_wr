"""Creates a graph."""


class DirectionalGraph(object):
    """Create a directional graph object."""

    def __init__(self):
        """."""
        self.node_list = []
        self.edges = {}

    def nodes(self):
        """Return a list of all nodes in the graph."""
        return self.node_list

    def edge_report(self):
        """Return a list of all edges in the graph."""
        return list(self.edges.key())

    def add_node(self, val):
        """Add a node to the graph."""
        self.node_list.append(val)

    def add_edge(self, val1, val2, wt=0):
        """Add new edge to graph connecting nodes "val1" and "val2"."""
        if val1 not in self.node_list:
            self.add_node(val1)
        if val2 not in self.node_list:
            self.add_node(val2)
        self.edges[(val1, val2)] = wt

    def del_node(self, val):
        """Del Node containing "val" from graph."""
        temp_edges = {}
        if val in self.node_list:
            self.node_list.remove(val)
            for key in self.edges.keys():
                if val not in key:
                    temp_edges[key] = self.edges[key]
            self.edges = temp_edges
        else:
            raise Exception("Node not in graph.")

    def del_edge(self, val1, val2):
        """Del edge connecting "val1" and "val2"."""
        if (val1, val2) in self.edges:
            del self.edges[(val1, val2)]
        else:
            raise Exception("Edge does not exist.")

    def has_node(self, val):
        """Return true of node w/ "val" is in the graph."""
        return (val in self.node_list)

    def neighbors(self, val):
        """Return list of all nodes connected to node with "val"."""
        temp_list = []
        for key in self.edges.keys():
            if val in key:
                if val == key[0]:
                    temp_list.append(key[1])
                else:
                    temp_list.append(key[0])
        return list(set(temp_list))

    def adjacent(self, val1, val2):
        """Return true if an edge connects "val1" and "val2"."""
        if (val1, val2) in self.edges:
            return True
        elif val1 or val2 in self.node_list:
            return False
        else:
            raise Exception('Neither of those are in the graph.')
