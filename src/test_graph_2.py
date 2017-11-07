"""."""
import pytest


@pytest.fixture
def basic_setup():
    """A basic setup with an empty graph."""
    from graph_1 import DirectionalGraph
    graph = DirectionalGraph()
    return graph


@pytest.fixture
def populated_graph():
    """A graph populated with nodes but no edges."""
    from graph_1 import DirectionalGraph
    graph = DirectionalGraph()
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    graph.add_node(4)
    return graph


@pytest.fixture
def populated_edges_graph():
    """A graph populated with nodes & edges."""
    from graph_1 import DirectionalGraph
    graph = DirectionalGraph()
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    graph.add_node(4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 4)
    graph.add_edge(3, 2)
    graph.add_edge(4, 1)
    return graph


def test_empty_graph_is_empty(basic_setup):
    """Make sure basic graph instantiates with null values."""
    assert basic_setup.node_list == []
    assert basic_setup.edges == {}


def test_add_node_populates_graph(basic_setup):
    """Add node works."""
    basic_setup.add_node(1)
    assert basic_setup.node_list[0] == 1


def test_del_node_removes_it(populated_graph):
    """Del node will get rid of a node."""
    populated_graph.del_node(1)
    print(populated_graph.node_list)
    assert len(populated_graph.node_list) == 3


def nodes_works(populated_graph):
    """The function properly displays a list of nodes."""
    assert populated_graph.nodes == [1, 2, 3, 4]


def test_all_nodes_removed_raises_no_error(populated_graph):
    """Deleting all the nodes will leave an empty node list."""
    populated_graph.del_node(1)
    populated_graph.del_node(2)
    populated_graph.del_node(3)
    populated_graph.del_node(4)
    assert populated_graph.node_list == []


def edges_returns_the_edge_list(populated_edges_graph):
    """The method will return the proper list of tuples."""
    assert populated_edges_graph.edges == [(1, 2), (1, 4), (3, 2), (4, 1)]


def test_add_edge_works(populated_graph):
    """Adding an edge will establish said edge."""
    populated_graph.add_edge(1, 2)
    assert (1, 2) in populated_graph.edges


def test_removing_edge_removes_from_dict(populated_edges_graph):
    """You can remove an edge."""
    populated_edges_graph.del_edge(3, 2)
    assert (3, 2) not in populated_edges_graph.edges


def test_removing_edge_only_removes__edge_from_dict(populated_edges_graph):
    """Removing an edge will leave the rest intact."""
    populated_edges_graph.del_edge(3, 2)
    assert (1, 2) in populated_edges_graph.edges


def test_del_node_removes_edges_common_to_node(populated_edges_graph):
    """Deleting a node will remove the edges it has."""
    populated_edges_graph.del_node(1)
    assert len(populated_edges_graph.edges) == 1


def test_del_node_retains_weight_of_remaining_keys(populated_edges_graph):
    """Deleting a node will remove the edges it has."""
    populated_edges_graph.del_node(1)
    assert populated_edges_graph.edges[(3, 2)] == 0


def test_neighbors_works_as_intended(populated_edges_graph):
    """Neighbor will register."""
    assert populated_edges_graph.neighbors(1) == [2, 4]


def test_adjacent_works(populated_edges_graph):
    """Adjacent knows that an edge connects something."""
    assert populated_edges_graph.adjacent(1, 2)


def test_adjacent_wont_return_false_positive(populated_edges_graph):
    """Adjacent won't return a false positive."""
    assert not populated_edges_graph.adjacent(3, 1)


def test_has_node_registers_true(populated_graph):
    """Node registers true when it should."""
    assert populated_graph.has_node(1)


def test_has_node_registers_false(populated_graph):
    """Will not return a false positive."""
    assert not populated_graph.has_node('spaghetti')


def test_del_node_raises_index_error(populated_graph):
    """Won't delete something that isn't there."""    
    with pytest.raises(IndexError):
        populated_graph.del_node('tortoise')


def test_adding_nodes_through_edges_works(basic_setup):
    """."""
    basic_setup.add_edge(1, 2)
    basic_setup.add_node(1)
    basic_setup.add_node(2)
    assert basic_setup.node_list == [1, 2]
    
