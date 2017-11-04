"""Make a minimum binheap."""


class Binheap(object):
    """Initialize a new instance of a bin heap."""

    def __init__(self, iterable=()):
        """Instantiate a new bin heap."""
        self.bin_list = [0]
        self.heap_index = 0
        if hasattr(iterable, '__iter__') or isinstance(iterable, str):
            for item in iterable:
                self.push(item)

    def display(self):
        """Print the contents of the heap."""
        print(self.bin_list[1:])

    def push(self, data):
        """Push a new item to the end of the list."""
        self.bin_list.append(data)
        self.heap_index += 1
        self.sort(self.heap_index)

    def sort(self, index):
        """Sort from the bottom of the list up."""
        range = self.heap_index
        while range > 0:
            if (index // 2) > 0:
                if self.bin_list[index] < self.bin_list[index // 2]:
                    temp = self.bin_list[index // 2]
                    self.bin_list[index // 2] = self.bin_list[index]
                    self.bin_list[index] = temp
                    index = index // 2
            range -= 1

    def sort_down(self):
        """."""
        index = 1
        while self.bin_list[index * 2]:
            if self.bin_list[index * 2] and self.bin_list[index * 2 + 1]:
                if (self.bin_list[index * 2]) > (self.bin_list[index * 2 + 1]):
                    child_idx = (index * 2) + 1
                else:
                    child_idx = index * 2
            elif self.bin_list[index * 2]:
                child_idx = index * 2
            parent = self.bin_list[index]
            if self.bin_list[index] > self.bin_list[child_idx]:
                self.bin_list[index] = self.bin_list[child_idx]
            self.bin_list[child_idx] = parent
            index = child_idx
