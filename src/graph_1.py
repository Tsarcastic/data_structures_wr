"""."""


# class GraphNode(object):
#     """Create a graph node object."""

#     def __init__(self, value):
#         """."""
#         self.value = value


class DirectionalGraph(object):
    """Create a directional graph object."""

    def __init__(self):
        """."""
        self.node_list = []
        self.edges = {}

    def nodes(self):
        """Return a list of all nodes in the graph."""
        return self.node_list

    def edges(self):
        """Return a list of all edges in the graph."""
        return list(self.edges.key())

    def add_node(self, val):
        """Add a node to the graph."""
        self.node_list.append(val)

    def add_edge(self, val1, val2, wt=0):
        """Add new edge to graph connecting nodes "val1" and "val2"."""
        self.edges[(val1, val2)] = wt

    def del_node(self, val):
        """Del Node containing "val" from graph."""
        if val in self.node_list:
            self.node_list.remove(val)
            for key in self.edges.keys():
                if val in key:
                    del self.edges[key]
        else:
            raise IndexError("Node not in graph.")

    def del_edge(self, val1, val2):
        """Del edge connecting "val1" and "val2"."""
        if (val1, val2) in self.edges:
            del self.edges[(val1, val2)]
        else:
            raise IndexError("Edge does not exist.")

    def has_node(self, val):
        """Return true of node w/ "val" is in the graph."""
        if val in self.node_list:
            return True
        else:
            return False

    def neighbors(self, val):
        """Return list of all nodes connedted to node with "val"."""
        temp_list = []
        for key in self.edges.keys():
            if val in key:
                temp_list.append(val)
        return temp_list

    def adjacent(self, val1, val2):
        """Return true if an edge connects "val1" and "val2"."""
