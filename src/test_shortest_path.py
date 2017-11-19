"""."""


def test_4_nodes_dist():
    """A basic setup with an empty graph."""
    import pytest
    from djs_algorithm import djs_algorithm 
    nodelist = ['a', 'b', 'c', 'd']
    edges = {('a', 'c'): 8,
             ('a', 'b'): 4,
             ('b', 'd'): 2,
             ('c', 'd'): 4,
             }
    dist, route = djs_algorithm('a', 'd', nodelist, edges)
    assert dist == 6


def test_4_nodes_list():
    """A basic setup with an empty graph."""
    from djs_algorithm import djs_algorithm 
    import pytest
    nodelist = ['a', 'b', 'c', 'd']
    edges = {('a', 'c'): 8,
             ('a', 'b'): 4,
             ('b', 'd'): 2,
             ('c', 'd'): 4,
             }
    dist, route = djs_algorithm('a', 'd', nodelist, edges)
    assert route == ['a', 'b', 'd']


def test_4_nodes_list02():
    """A basic setup with an empty graph."""
    from djs_algorithm import djs_algorithm 
    import pytest
    nodelist = ['a', 'b', 'c', 'd']
    edges = {('a', 'c'): 8,
             ('a', 'b'): 4,
             ('b', 'd'): 2,
             ('c', 'd'): 4,
             }
    dist, route = djs_algorithm('c', 'd', nodelist, edges)
    assert route == ['c', 'd']