"""."""

import pytest


def test_node_exists_in_continuum01():
    """Test for previous."""
    from double_linked_list import Node, DoubleLinkedList
    dll = DoubleLinkedList()
    dll.push('banana')
    dll.push('orange')
    assert dll.head.next_node.previous.data == 'orange'


def test_node_exists_in_continuum02():
    """Test for previous."""
    from double_linked_list import Node, DoubleLinkedList
    dll = DoubleLinkedList()
    dll.push('banana')
    dll.push('orange')
    assert dll.head.next_node.data == 'banana'


def test_node_exists_in_continuum03():
    """Test for previous."""
    from double_linked_list import Node, DoubleLinkedList
    dll = DoubleLinkedList()
    dll.push('banana')
    dll.push('orange')
    assert dll.head.next_node.next_node is None


def test_pop_off_01():
    """Pop one off and return correct value."""
    from double_linked_list import Node, DoubleLinkedList
    dll = DoubleLinkedList()
    dll.push('banana')
    dll.push('orange')
    dll.pop()
    assert dll.head.data == 'banana'


def test_pop_off_02():
    """Pop one off and return correct value."""
    from double_linked_list import Node, DoubleLinkedList
    dll = DoubleLinkedList()
    dll.push('banana')
    dll.push('orange')
    dll.pop()
    assert not dll.head.previous


def test_shift_from_tail_changes_length():
    """Can push 2 remove 1 and length is 1."""
    from double_linked_list import Node, DoubleLinkedList
    dll = DoubleLinkedList()
    dll.push('banana')
    dll.push('orange')
    dll.shift()
    assert len(dll) == 1


def test_shift_from_tail_removes_last():
    """Push 2 in, shift one and data is correct."""
    from double_linked_list import Node, DoubleLinkedList
    dll = DoubleLinkedList()
    dll.push('banana')
    dll.push('orange')
    dll.shift()
    assert dll.tail.data == "orange"


def test_shift_from_tail_one_item_head_is_tail():
    """Tail is correct."""
    from double_linked_list import Node, DoubleLinkedList
    dll = DoubleLinkedList()
    dll.push('banana')
    dll.push('orange')
    dll.shift()
    assert dll.tail == dll.head


def test_shift_on_empty_list_raises_exception():
    """Shift on empty list raises exception."""
    from double_linked_list import Node, DoubleLinkedList
    dll = DoubleLinkedList()
    with pytest.raises(IndexError):
        dll.shift()


def test_append_on_empty_list_makes_head_and_tail_same():
    """Appending an item to an empty list makes that item head and tail."""
    from double_linked_list import Node, DoubleLinkedList
    dll = DoubleLinkedList()
    dll.append("blue")
    assert dll.head == dll.tail


def test_append_increments_counter():
    """Size goes up correctly."""
    from double_linked_list import Node, DoubleLinkedList
    dll = DoubleLinkedList()
    dll.append("blue")
    assert dll.size() == 1


def test_append_changes_tail_when_list_has_multiple_nodes():
    """Tail shifts correctly when appended."""
    from double_linked_list import Node, DoubleLinkedList
    dll = DoubleLinkedList()
    dll.append("blue")
    dll.append("red")
    assert dll.tail.data != "blue"


def test_append_retains_correct_next_node_for_nodes():
    """A node's 'next_node' is retained properly through appending."""
    from double_linked_list import Node, DoubleLinkedList
    dll = DoubleLinkedList()
    dll.append("blue")
    dll.append("red")
    assert dll.head.next_node.data == "red"


def test_remove01():
    """Removing an item maintains list."""
    from double_linked_list import Node, DoubleLinkedList
    dll = DoubleLinkedList()
    dll.push('z')
    dll.push('x')
    dll.push('y')
    dll.remove('x')
    assert dll.head.next_node.data == 'z'


def test_remove02():
    """The tail is correctly updated when the previous tail is removed."""
    from double_linked_list import Node, DoubleLinkedList
    dll = DoubleLinkedList()
    dll.push('x')
    dll.push('z')
    dll.push('x')
    dll.push('y')
    dll.remove('x')
    assert dll.tail.data == 'x'


def test_display():
    """Will return the correct string representing double linked list."""
    from double_linked_list import Node, DoubleLinkedList
    dll = DoubleLinkedList()
    dll.push('x')
    dll.push('z')
    dll.push('x')
    dll.push('y')
    assert dll.display() == "(y, x, z, x)"

