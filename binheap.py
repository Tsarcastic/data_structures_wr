"""Make a minimum binheap."""


class BinHeap(object):
    """Initialize a new instance of a bin heap."""

    def __init__(self):
        """Instantiate a new bin heap."""
        self.bin_list = [0]
        self.heap_index = 0

    def push(self, data):
        """Push a new item to the end of the list."""
        self.bin_list.append(data)
        self.heap_index += 1
        self.sort(self.heap_index)

    def sort(self, index):
        """Sort from the bottom of the list up."""
        while (index // 2) > 0:
            if self.bin_list[index] < self.bin_list[index // 2]:
                temp = self.bin_list[index // 2]
                self.bin_list[index // 2] = self.bin_list[index]
                self.bin_list[index] = temp
                index = index // 2
