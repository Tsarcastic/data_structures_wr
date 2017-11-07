"""Module to implement graph traversal."""


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
                if val == key[0]:
                    temp_list.append(key[1])
                else:
                    temp_list.append(key[0])
        return list(set(temp_list))

    def adjacent(self, val1, val2):
        """Return true if an edge connects "val1" and "val2"."""
        if (val1, val2) in self.edges or (val2, val1) in self.edges:
            return True
        else:
            return False

    def breadth_first(self, starting):
        """Traverse the graph breadth-first."""
        visited = {}
        answer = []
        q = []
        for item in self.node_list:
            visited[item] = False
        q.append(starting)
        while len(q) > 0:
            for edge in self.edges:
                if (edge[0] == q[0]) and not (visited[edge[1]]):
                    q.append(edge[1])
            answer.append(q[0])
