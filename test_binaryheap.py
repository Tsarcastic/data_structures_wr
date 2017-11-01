"""Run tests to check binary heap for proper operation."""


def test_pop_from_empty_heap_raises_exception():
    pass

def test_append_adds_value_to_heap():
    heap.push(val) 
    assert heap.bin_list.contains(val)

def test_pop_removes_value_from_heap():
    value = heap.pop()
    assert  value not in heap.bin_list

def test_children_are_less_than_parents():
    assert child1 value < parent value
    assert child2 value < parent value