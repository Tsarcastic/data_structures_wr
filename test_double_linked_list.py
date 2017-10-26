"""."""

import pytest


def test_node_exists_in_continuum01():
    """Test for previous."""
    from double_linked_list import Node, DoubleLinkedList
    dll = DoubleLinkedList()
    dll.push('banana')
    dll.push('orange')
    assert dll.head.next.previous.data == 'orange'


def test_node_exists_in_continuum02():
    """Test for previous."""
    from double_linked_list import Node, DoubleLinkedList
    dll = DoubleLinkedList()
    dll.push('banana')
    dll.push('orange')
    assert dll.head.next.data == 'banana'


def test_node_exists_in_continuum03():
    """Test for previous."""
    from double_linked_list import Node, DoubleLinkedList
    dll = DoubleLinkedList()
    dll.push('banana')
    dll.push('orange')
    assert dll.head.next.next is None


def test_pop_off_01():
    from double_linked_list import Node, DoubleLinkedList
    dll = DoubleLinkedList()
    dll.push('banana')
    dll.push('orange')
    dll.pop()
    assert dll.head.data == 'banana'


def test_pop_off_02():
    from double_linked_list import Node, DoubleLinkedList
    dll = DoubleLinkedList()
    dll.push('banana')
    dll.push('orange')
    dll.pop()
    assert not dll.head.previous


def test_shift_from_tail_changes_length():
    from double_linked_list import Node, DoubleLinkedList
    dll = DoubleLinkedList()
    dll.push('banana')
    dll.push('orange')
    dll.shift()
    assert len(dll) == 1


def test_shift_from_tail_removes_last():
    from double_linked_list import Node, DoubleLinkedList
    dll = DoubleLinkedList()
    dll.push('banana')
    dll.push('orange')
    dll.shift()
    assert dll.tail.data == "orange"


def test_shift_from_tail_one_item_head_is_tail():
    from double_linked_list import Node, DoubleLinkedList
    dll = DoubleLinkedList()
    dll.push('banana')
    dll.push('orange')
    dll.shift()
    assert dll.tail == dll.head


def test_shift_on_empty_list_raises_exception():
    from double_linked_list import Node, DoubleLinkedList
    dll = DoubleLinkedList()
    with pytest.raises(IndexError):
        dll.shift()


def test_append_on_empty_list_makes_head_and_tail_same():
    from double_linked_list import Node, DoubleLinkedList
    dll = DoubleLinkedList()
    dll.append("blue")
    assert dll.head == dll.tail


def test_append_increments_counter():
    from double_linked_list import Node, DoubleLinkedList
    dll = DoubleLinkedList()
    dll.append("blue")
    assert dll.size() == 1


def test_append_changes_tail_when_list_has_multiple_nodes():
    from double_linked_list import Node, DoubleLinkedList
    dll = DoubleLinkedList()
    dll.append("blue")
    dll.append("red")
    assert dll.tail.data != "blue"
























def test_remove01():
    from double_linked_list import Node, DoubleLinkedList
    dll = DoubleLinkedList()
    dll.push('z')
    dll.push('x')
    dll.push('y')
    dll.remove('x')
    assert dll.head.next.data == 'z'

def test_remove02():
    from double_linked_list import Node, DoubleLinkedList
    dll = DoubleLinkedList()
    dll.push('x')
    dll.push('z')
    dll.push('x')
    dll.push('y')
    dll.remove('x')
    assert dll.tail.data == 'x'

