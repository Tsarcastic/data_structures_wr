"""Run tests to check binary heap for proper operation."""
import pytest


@pytest.fixture
def basic_setup():
    """A basic setup with an empty heap."""
    from binheap import Binheap
    heap = Binheap()
    return heap


@pytest.fixture
def loaded_setup():
    """A heap loaded with nodes."""
    from binheap import Binheap
    heap = Binheap((1, 3, 6, 9, 22, 100, 53))
    return heap


def test_pop_from_empty_heap_raises_exception(basic_setup):
    """Popping an empty node raises exception."""
    with pytest.raises(IndexError):
        basic_setup.pop()


def test_push_adds_value_to_heap(basic_setup):
    """Pushing one value in works."""
    basic_setup.push(24)
    assert 24 in basic_setup.bin_list


def test_pop_removes_value_from_heap(loaded_setup):
    """Popping an item from a heap removes it."""
    value = loaded_setup.pop()
    assert value not in loaded_setup.bin_list


def test_heap_pops_values_in_ascending_order(loaded_setup):
    """Popping items from a heap will do it in the correct order."""
    output = []
    for number in range(1, 8):
        output.append(loaded_setup.pop())
    assert output == [1, 3, 6, 9, 22, 53, 100]


def test_correct_structure_maintained(basic_setup):
    """Pushing items of non-contiguous values will maintain heap structure."""
    basic_setup.push(7)
    basic_setup.push(14)
    basic_setup.push(5)
    basic_setup.push(1)
    basic_setup.push(6)
    basic_setup.push(8)
    assert basic_setup.bin_list == [0, 1, 5, 7, 14, 6, 8]


def test_correct_structure_with_appends(basic_setup):
    """Just more tests of the basic structure."""
    basic_setup.push(99)
    basic_setup.push(13)
    basic_setup.push(6)
    basic_setup.push(1)
    basic_setup.push(5)
    basic_setup.push(14)
    basic_setup.push(7)
    assert basic_setup.bin_list == [0, 1, 5, 7, 99, 6, 14, 13]


def test_returns_values_in_ascending_order(basic_setup):
    """The binheap constructed above will pop the lowest item each time."""
    output = []
    basic_setup.push(99)
    basic_setup.push(13)
    basic_setup.push(6)
    basic_setup.push(1)
    basic_setup.push(5)
    basic_setup.push(14)
    basic_setup.push(7)
    for number in range(7):
        output.append(basic_setup.pop())
    assert output == [1, 5, 6, 7, 13, 14, 99]
    #assert basic_setup.bin_list == [0, 6, 13, 7, 99, 14]