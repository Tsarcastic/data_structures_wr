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


@pytest.fixture
def tricky_setup():
    """A heap to build from."""
    from binheap import Binheap
    heap = Binheap((5, 19, 33, 1, 3))
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


def test_correct_structure_with_appends01(basic_setup):
    """Pushing items of non-contiguous values will maintain heap structure."""
    basic_setup.push(7)
    basic_setup.push(14)
    basic_setup.push(5)
    basic_setup.push(1)
    basic_setup.push(6)
    basic_setup.push(8)
    assert basic_setup.bin_list == [0, 1, 5, 7, 14, 6, 8]


def test_returns_values_in_ascending_order01(basic_setup):
    """Item returned will always be the smallest number in the heap."""
    output = []
    basic_setup.push(7)
    basic_setup.push(14)
    basic_setup.push(5)
    basic_setup.push(1)
    basic_setup.push(6)
    basic_setup.push(8)
    for number in range(basic_setup.heap_index):
        output.append(basic_setup.pop())
    assert output == [1, 5, 6, 7, 8, 14]


def test_correct_structure_with_appends02(basic_setup):
    """Just more tests of the basic structure."""
    basic_setup.push(99)
    basic_setup.push(13)
    basic_setup.push(6)
    basic_setup.push(1)
    basic_setup.push(5)
    basic_setup.push(14)
    basic_setup.push(7)
    assert basic_setup.bin_list == [0, 1, 5, 7, 99, 6, 14, 13]


def test_returns_values_in_ascending_order02(basic_setup):
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


def test_correct_structure_with_pushes_and_pops01(tricky_setup):
    """Push and pop alternate irregularly."""
    tricky_setup.pop()
    assert tricky_setup.bin_list == [0, 3, 5, 33, 19]


def test_correct_structure_with_pushes_and_pops02(tricky_setup):
    """Push and pop alternate irregularly."""
    tricky_setup.pop()
    tricky_setup.push(2)
    assert tricky_setup.bin_list == [0, 2, 3, 33, 19, 5]


def test_correct_structure_with_pushes_and_pops03(tricky_setup):
    """Push and pop alternate irregularly."""
    tricky_setup.pop()
    tricky_setup.push(2)
    tricky_setup.push(44)
    assert tricky_setup.bin_list == [0, 2, 3, 33, 19, 5, 44]


def test_correct_structure_with_pushes_and_pops04(tricky_setup):
    """Push and pop alternate irregularly."""
    tricky_setup.pop()
    tricky_setup.push(2)
    tricky_setup.push(44)
    tricky_setup.pop()
    assert tricky_setup.bin_list == [0, 3, 5, 33, 19, 44]


def test_correct_structure_with_pushes_and_pops05(tricky_setup):
    """Push and pops alternate irregularly."""
    tricky_setup.pop()
    tricky_setup.push(2)
    tricky_setup.push(44)
    tricky_setup.pop()
    tricky_setup.push(4)
    assert tricky_setup.bin_list == [0, 3, 5, 4, 19, 44, 33]


def test_correct_structure_with_pushes_and_pops06(tricky_setup):
    """Push and pop alternate irregularly."""
    tricky_setup.pop()
    tricky_setup.push(2)
    tricky_setup.push(44)
    tricky_setup.pop()
    tricky_setup.push(4)
    assert tricky_setup.bin_list == [0, 3, 5, 4, 19, 44, 33]


def tricky_setup_will_always_return_lowest(tricky_setup):
    """Push and pop alternate irregularly."""
    output = []
    tricky_setup.pop()
    tricky_setup.push(2)
    tricky_setup.push(44)
    tricky_setup.pop()
    tricky_setup.push(4)
    for number in range(basic_setup.heap_index):
        output.append(basic_setup.pop())
    assert output == [3, 4, 5, 19, 33, 44]


def test_will_maintain_structure_at_large_lengths(basic_setup):
    """Push and pop alternate irregularly."""
    basic_setup.push(1)
    basic_setup.push(17)
    basic_setup.push(9)
    basic_setup.push(13)
    basic_setup.push(33)
    basic_setup.push(2)
    basic_setup.push(19)
    basic_setup.push(16)
    basic_setup.push(53)
    basic_setup.push(3)
    basic_setup.push(4)
    assert basic_setup.bin_list == [0, 1, 3, 2, 16, 4, 9, 19, 17, 53, 33, 13]


def test_large_lengths_will_always_pop_lowest(basic_setup):
    """The heap can maintain its size."""
    output = []
    basic_setup.push(1)
    basic_setup.push(17)
    basic_setup.push(9)
    basic_setup.push(13)
    basic_setup.push(33)
    basic_setup.push(2)
    basic_setup.push(19)
    basic_setup.push(16)
    basic_setup.push(53)
    basic_setup.push(3)
    basic_setup.push(4)
    basic_setup.push(99)
    for number in range(basic_setup.heap_index):
        output.append(basic_setup.pop())
    assert output == [1, 2, 3, 4, 9, 13, 16, 17, 19, 33, 53, 99]
