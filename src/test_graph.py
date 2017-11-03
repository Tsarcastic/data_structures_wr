"""."""
import pytest

@pytest.fixture
def basic_setup():
    from graph_1 import DirectionalGraph
    graph = DirectionalGraph()
    return graph

@pytest.fixture
def populated_graph():
    from graph_1 import DirectionalGraph
    graph = DirectionalGraph()
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    graph.add_node(4)
    return graph

@pytest.fixture
def populated_edges_graph():
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
    basic_setup.add_node(1)
    assert basic_setup.node_list[0] == 1

def test_del_node_removes_it(populated_graph):
    populated_graph.del_node(1)
    print(populated_graph.node_list)
    assert len(populated_graph.node_list) == 3

def test_all_nodes_removed_raises_no_error(populated_graph):
    populated_graph.del_node(1)
    populated_graph.del_node(2)
    populated_graph.del_node(3)
    populated_graph.del_node(4)
    assert populated_graph.node_list == []

def test_add_edge_works(populated_graph):
    populated_graph.add_edge(1,2)
    assert (1, 2) in populated_graph.edges

def test_removing_edge_removes_from_dict(populated_edges_graph):
    populated_edges_graph.del_edge(3, 2)
    assert (3, 2) not in populated_edges_graph.edges

def test_removing_edge_only_removes_given_edge_from_dict(populated_edges_graph):
    populated_edges_graph.del_edge(3, 2)
    assert (1, 2) in populated_edges_graph.edges

def test_del_node_removes_edges_common_to_node(populated_edges_graph):
    populated_edges_graph.del_node(1)
    assert len(populated_edges_graph.edges) == 1