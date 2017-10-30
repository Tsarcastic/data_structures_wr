"""."""

import pytest


def test_node_exists_in_continuum01():
    """Test for previous."""
    from deque import Node, Deque
    dq = Deque()
    dq.append_left('banana')
    dq.append_left('orange')
    assert dq.head.next_node.previous.data == 'orange'


def test_node_exists_in_continuum02():
    """Test for previous."""
    from deque import Node, Deque
    dq = Deque()
    dq.append_left('banana')
    dq.append_left('orange')
    assert dq.head.next_node.data == 'banana'


def test_node_exists_in_continuum03():
    """Test for previous."""
    from deque import Node, Deque
    dq = Deque()
    dq.append_left('banana')
    dq.append_left('orange')
    assert dq.head.next_node.next_node is None


def test_pop_left_off_01():
    """Pop one off and return correct value."""
    from deque import Node, Deque
    dq = Deque()
    dq.append_left('banana')
    dq.append_left('orange')
    dq.popleft()
    assert dq.head.data == 'banana'


def test_pop_off_02():
    """Pop one off and return correct value."""
    from deque import Node, Deque
    dq = Deque()
    dq.append_left('banana')
    dq.append_left('orange')
    dq.popleft()
    assert not dq.head.previous


def test_shift_from_tail_changes_length():
    """Can append_left 2 remove 1 and length is 1."""
    from deque import Node, Deque
    dq = Deque()
    dq.append_left('banana')
    dq.append_left('orange')
    dq.pop()
    assert len(dq) == 1


def test_pop_from_tail_removes_last():
    """append_left 2 in, pop one and data is correct."""
    from deque import Node, Deque
    dq = Deque()
    dq.append_left('banana')
    dq.append_left('orange')
    dq.pop()
    assert dq.tail.data == "orange"


def test_pop_from_tail_one_item_head_is_tail():
    """Tail is correct."""
    from deque import Node, Deque
    dq = Deque()
    dq.append_left('banana')
    dq.append_left('orange')
    dq.pop()
    assert dq.tail == dq.head


def test_pop_on_empty_deque_raises_exception():
    """Shift on empty deque raises exception."""
    from deque import Node, Deque
    dq = Deque()
    with pytest.raises(IndexError):
        dq.pop()


def test_popleft_on_empty_deque_raises_exception():
    """Shift on empty deque raises exception."""
    from deque import Node, Deque
    dq = Deque()
    with pytest.raises(IndexError):
        dq.popleft()


def test_append_on_deque_makes_head_and_tail_same():
    """Appending an item to an empty deque makes that item head and tail."""
    from deque import Node, Deque
    dq = Deque()
    dq.append("blue")
    assert dq.head == dq.tail


def test_append_left_on_deque_makes_head_and_tail_same():
    """Appending an item to an empty deque makes that item head and tail."""
    from deque import Node, Deque
    dq = Deque()
    dq.append_left("blue")
    assert dq.head == dq.tail

def test_append_increments_counter():
    """Size goes up correctly."""
    from deque import Node, Deque
    dq = Deque()
    dq.append("blue")
    assert dq.size() == 1


def test_pop_left_decreases_counter():
    """Size goes down correctly."""
    from deque import Node, Deque
    dq = Deque()
    dq.append("blue")
    dq.popleft()
    assert dq.size() == 0


def test_pop_decreases_counter():
    """Size goes down correctly."""
    from deque import Node, Deque
    dq = Deque()
    dq.append("blue")
    dq.pop()
    assert dq.size() == 0

def test_append_left_increments_counter():
    """Size goes up correctly."""
    from deque import Node, Deque
    dq = Deque()
    dq.append_left("blue")
    assert dq.size() == 1


def test_append_changes_tail_when_deque_has_multiple_nodes():
    """Tail shifts correctly when appended."""
    from deque import Node, Deque
    dq = Deque()
    dq.append("blue")
    dq.append("red")
    assert dq.tail.data != "blue"


def test_append_retains_correct_next_node_for_nodes():
    """A node's 'next_node' is retained properly through appending."""
    from deque import Node, Deque
    dq = Deque()
    dq.append("blue")
    dq.append("red")
    assert dq.head.next_node.data == "red"

def test_deque_head_equals_tail():
    """An empty node's head and tail are equal."""
    from deque import Node, Deque    
    dq = Deque()
    assert dq.head == dq.tail


def test_peek_returns_value_of_tail():
    """Peeking will return the value of the tail."""
    from deque import Node, Deque
    dq = Deque()
    dq.append("blue")
    dq.append("red")
    assert dq.peek() ==  'red'

def test_peek_left_returns_value_of_head():
    """Peeking will return the value of the tail."""
    from deque import Node, Deque
    dq = Deque()
    dq.append("blue")
    dq.append("red")
    assert dq.peekleft() == 'blue'
