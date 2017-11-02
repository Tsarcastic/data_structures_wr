"""."""


class GraphNode(object):
    """Create a graph node object."""

    def __init__(self, value):
        """."""
        self.value = value
        self.edges = {}


class DirectionalGraph(object):
    """Create a directional graph object."""

    def __init__(self):
        """."""
        self.node_list = []

    def nodes(self):
        """Return a list of all nodes in the graph."""

    def edges(self):
        """Return a list of all edges in the graph."""

    def add_node(self, val):
        """Add a node to the graph."""

    def add_edge(self, val1, val2):
        """Add new edge to graph connecting nodes "val1" and "val2"."""

    def del_node(self, val):
        """Del Node containing "val" from graph."""

    def del_edge(self, val1, val2):
        """Del edge connecting "val1" and "val2"."""

    def has_node(self, val):
        """Return true of node w/ "val" is in the graph."""

    def neighbors(self, val):
        """Return list of all nodes connedted to node with "val"."""

    def adjacent(self, val1, val2):
        """Return true if an edge connects "val1" and "val2"."""
