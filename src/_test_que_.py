"""Test for the queue."""


import pytest


def test_node_has_attributes():
    """Test for Node."""
    from que_ import Node
    n = Node(1, None)
    assert hasattr(n, 'data')
    assert hasattr(n, 'data')


def test_empty_queue_does_not_have_head():
    """."""
    from que_ import Queue
    q = Queue()
    assert q.head is None


def test_empty_queue_does_not_have_tail():
    """."""
    from que_ import Queue
    q = Queue()
    assert q.tail is None


def test_enque_creates_head():
    """."""
    from que_ import Queue
    q = Queue()
    q.enqueue('x')
    assert q.head.data is 'x'


def test_enque_creates_tail():
    """."""
    from que_ import Queue
    q = Queue()
    q.enqueue('x')
    assert q.tail.data is 'x'


def test_two_items_in_line_correct_head():
    """If two items queue up the head is the first."""
    from que_ import Queue
    q = Queue()
    q.enqueue('x')
    q.enqueue('y')
    assert q.head.data is 'x'


def test_two_items_in_line_correct_tail():
    """If two items queue up the tail is the second one."""
    from que_ import Queue
    q = Queue()
    q.enqueue('x')
    q.enqueue('y')
    assert q.tail.data is 'y'


def test_dequeue_error_message():
    """If two items queue up and one dequeues the second is the new head."""
    from que_ import Queue
    q = Queue()
    q.enqueue('x')
    q.enqueue('y')
    q.enqueue('z')
    q.dequeue()
    assert q.head.data == 'y'


def test_len_works_properly():
    """If two items queue up and one dequeues the second is the new head."""
    from que_ import Queue
    q = Queue()
    q.enqueue('x')
    q.enqueue('y')
    assert len(q) == 2


def peek_works():
    """Peekaboo."""
    from que_ import Queue
    q = Queue()
    q.enqueue('x')
    q.enqueue('y')
    assert q.peek == 'x'


def test_size_works_properly():
    """If two items queue up and one dequeues the second is the new head."""
    from que_ import Queue
    q = Queue()
    q.enqueue('x')
    q.enqueue('y')
    assert q.size() == 2

def test_next_is_correct():
    """If two items queue up and one dequeues the second is the new head."""
    from que_ import Queue
    q = Queue()
    q.enqueue('x')
    q.enqueue('y')
    assert q.size() == 2