"""test for Singly linked list."""


import pytest


def test_node_has_attributes():
    """Test for Node."""
    from linked_list import Node
    n = Node(1, None)
    assert hasattr(n, 'data')
    assert hasattr(n, 'data')


def test_linked_list_has_head():
    """Test linked list has nead attr."""
    from linked_list import LinkedList
    l = LinkedList()
    assert l.head is None


def test_linked_list_push_adds_new_item():
    """Test that push adds item to list."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push('val')
    assert l.head.data == 'val'


def test_linked_list_push_two_new_item():
    """Test pushing 2 values to list works."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push('val')
    l.push('val2')
    assert l.head.data == 'val2'


def test_linked_list_push_moves_old_head_to_new_heads_next():
    """Test when pushing mult values, head moves."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push('val')
    l.push('val2')
    assert l.head.next.data == 'val'


def test_linked_list_pop_removes_head():
    """Test that pop removes head."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push('potato')
    l.pop()
    assert l.head is None


def test_linked_list_pop_returns_head_value():
    """Test that pop returns the value of the node."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push('potato')
    assert l.pop() == ('potato')


def test_linked_list_pop_shifts_head_properly():
    """Test that pop shifts head."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push('potato')
    l.push('cabbage')
    l.pop()
    assert l.head.data == 'potato'


def test_linked_list_pop_empty_raises_exception():
    """Test that using pop on empty list raises exception."""
    from linked_list import LinkedList
    l = LinkedList()
    with pytest.raises(IndexError):
        l.pop()


def test_linked_list_size_returns_list_length():
    """Test that size returns list count."""
    from linked_list import LinkedList
    l = LinkedList()
    assert l.size() == 0


@pytest.mark.parametrize('n', range(100))
def test_linked_list_size_returns_list_length2(n):
    """Test that large list tracks size properly."""
    from linked_list import LinkedList
    l = LinkedList()
    for i in range(n):
        l.push(i)
    assert l.size() == n


def test_linked_list_search__empty_returns_none():
    """Test search on empty list returns None."""
    from linked_list import LinkedList
    l = LinkedList()
    assert l.search(1) is None


def test_linked_list_search__with_one_returns_node():
    """Test search on single node list returns node."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push(1)
    assert l.search(1) == l.head


def test_linked_list_search__with_one_bad_search():
    """Test search on empty list raises error."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push(1)
    with pytest.raises(ValueError):
        l.search(0)


def test_linked_list_can_take_iterable_str():
    """Test LL can instantiate with iterable string."""
    from linked_list import LinkedList
    a_name = "bilbo baggins"
    l = LinkedList(a_name)
    for item in a_name:
        assert l.search(item).data == item


def test_linked_list_can_take_iterable_range():
    """Test LL can instantiate with range."""
    from linked_list import LinkedList
    a_list = range(1, 20)
    l = LinkedList(a_list)
    for item in a_list:
        assert l.search(item).data == item


def test_linked_list_can_take_iterable_list():
    """Test LL can instantiate with list type."""
    from linked_list import LinkedList
    a_list = [4, 3, 2, 6, 4, 9, 8]
    l = LinkedList(a_list)
    for item in a_list:
        assert l.search(item).data == item


def test_remove_removes_number_from_list():
    """Test remove removes value from the list."""
    from linked_list import LinkedList
    a_list = [4, 3, 2, 6, 4, 9, 8]
    l = LinkedList(a_list)
    l.remove(l.search(6))
    assert len(l) == 6
    with pytest.raises(ValueError):
        l.search(6)


def test_display_on_empty_list():
    """Test display on empty list shows empty tuple-like-string."""
    from linked_list import LinkedList
    lst = LinkedList()
    assert lst.display() == "()"


def test_display_a_list():
    """Test display lists out node values."""
    from linked_list import LinkedList
    a_list = [4, 3, 2, 6, 4, 9, 8]
    l = LinkedList(a_list)
    assert l.display() == "(8, 9, 4, 6, 2, 3, 4)"
