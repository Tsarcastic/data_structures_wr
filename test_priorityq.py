"""Test for the queue."""


import pytest


def test_node_has_attributes():
    """Test for Node."""
    from priority_queue import Node
    n = Node(1, None)
    assert hasattr(n, 'data')
    assert hasattr(n, 'data')


def test_empty_queue_does_not_have_head():
    """."""
    from priority_queue import Priority_Q
    q = Priority_Q()
    assert q.head is None


def test_empty_queue_does_not_have_tail():
    """."""
    from priority_queue import Priority_Q
    q = Priority_Q()
    assert q.tail is None


def test_insert_creates_head():
    """."""
    from priority_queue import Priority_Q
    q = Priority_Q()
    q.insert('x')
    assert q.head.data is 'x'


def test_insert_creates_tail():
    """."""
    from priority_queue import Priority_Q
    q = Priority_Q()
    q.insert('x')
    assert q.tail.data is 'x'


def test_two_items_in_line_correct_head():
    """If two items queue up the head is the first."""
    from priority_queue import Priority_Q
    q = Priority_Q()
    q.insert('x')
    q.insert('y')
    assert q.head.data is 'x'


def test_two_items_in_line_correct_tail():
    """If two items queue up the tail is the second one."""
    from priority_queue import Priority_Q
    q = Priority_Q()
    q.insert('x')
    q.insert('y')
    assert q.tail.data is 'y'


def test_popping_leaves_correct_head():
    """If two items queue up and one dequeues the second is the new head."""
    from priority_queue import Priority_Q
    q = Priority_Q()
    q.insert('x')
    q.insert('y')
    q.insert('z')
    q.pop()
    assert q.head.data == 'y'


def test_len_works_properly():
    """If two items queue up and one dequeues the second is the new head."""
    from priority_queue import Priority_Q
    q = Priority_Q()
    q.insert('x')
    q.insert('y')
    assert len(q) == 2


def peek_works():
    """Peekaboo."""
    from priority_queue import Priority_Q
    q = Priority_Q()
    q.insert('x')
    q.insert('y')
    assert q.peek == 'x'


def test_size_works_properly():
    """If two items queue up and one dequeues the second is the new head."""
    from priority_queue import Priority_Q
    q = Priority_Q()
    q.insert('x')
    q.insert('y')
    assert q.size() == 2


def test_next_is_correct():
    """If two items queue up and one dequeues the second is the new head."""
    from priority_queue import Priority_Q
    q = Priority_Q()
    q.insert('x')
    q.insert('y')
    assert q.size() == 2


def priority_remove_works01():
    """If two items queue up and one dequeues the second is the new head."""
    from priority_queue import Priority_Q
    q = Priority_Q()
    q.insert('x', None, 0)
    q.insert('y', None, 1)
    assert q.pop() == 'x'


def priority_remove_works02():
    """If two items queue up and one dequeues the second is the new head."""
    from priority_queue import Priority_Q
    q = Priority_Q()
    q.insert('z', None, 0)
    q.insert('x', None, 0)
    q.insert('y', None, 1)
    assert q.pop() == 'z'


def priority_remove_works03():
    """If two items queue up and one dequeues the second is the new head."""
    from priority_queue import Priority_Q
    q = Priority_Q()
    q.insert('z', None, 2)
    q.insert('x', None, 2)
    q.insert('y', None, 0)
    assert q.pop() == 'y'
