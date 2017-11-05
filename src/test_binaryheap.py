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
    """."""
    with pytest.raises(IndexError):
        basic_setup.pop()


def test_push_adds_value_to_heap(basic_setup):
    """."""
    basic_setup.push(24)
    assert 24 in basic_setup.bin_list


def test_pop_removes_value_from_heap(loaded_setup):
    """."""
    value = loaded_setup.pop()
    assert value not in loaded_setup.bin_list


def test_heap_pops_values_in_ascending_order(loaded_setup):
    """."""
    output = []
    for number in range(1, loaded_setup.heap_index):
        output.append(loaded_setup.pop())
    assert output == [1, 3, 6, 9, 22, 53, 100]


# def test_display_func_prints_heap(loaded_setup):
#     assert loaded_setup.display
