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
    assert dll.head.next.next == None

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