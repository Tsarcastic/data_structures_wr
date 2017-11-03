"""."""
import pytest

@pytest.fixture(scope='module')
def basic_setup():
    from graph_1 import DirectionalGraph
    graph = DirectionalGraph()


def test_empty_graph_is_empty(basic_setup):
    """Make sure basic graph instantiates with null values."""
    assert graph.node_list == []
    assert graph.edges == {}
    