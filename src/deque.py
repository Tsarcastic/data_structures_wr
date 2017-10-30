"""."""


class Node(object):
    """Creates a node object."""

    def __init__(self, data, next_node, previous="None"):
        """Constructor for the Node object."""
        self.data = data
        self.next_node = next_node
        self.previous = previous


class Deque(object):
    """Class for containing object called Deque."""

    def __init__(self):
        """Constructor for the deque object."""
        self.head = None
        self.tail = None
        self._size = 0
        self.isempty = True

    def append_left(self, val):
        """Add a new value to the head of the deque."""
        new_head = Node(val, self.head)
        if self.head is None:
            self.tail = new_head
            self.head = new_head
        else:
            self.head.previous = new_head
            self.head = new_head
        self._size += 1

    def append(self, val):
        """Add a node to the tail of the queue."""
        new_tail = Node(val, None, self.tail)
        if self.tail is None:
            self.head = new_tail
            self.tail = new_tail
        else:
            self.tail.next_node = new_tail
            self.tail = new_tail
        self._size += 1

    def popleft(self):
        """Remove & return the value of the head of the deque."""
        if not self.head:
            raise IndexError("The deque is empty, so there's nothing to pop.")
        elif self.head == self.tail:
            output = self.tail.data
            self.head = None
            self.tail = None
            self._size -= 1
            return output
        else:
            output = self.head.data
            self.head.next_node.previous = None
            self.head = self.head.next_node
            self._size -= 1
            return output

    def pop(self):
        """Remove last node from deque."""
        if not self.tail:
            raise IndexError("The deque is empty, so there's nothing to pop.")
        elif self.head == self.tail:
            temp = self.tail.data
            self.head = None
            self.tail = None
            self._size -= 1
            return temp
        else:
            temp = self.tail.data
            self.tail = self.tail.previous
            self.tail.next_node = None
            self._size -= 1
            return temp

    def __len__(self):
        """Work with len() function to find length of deque."""
        return self._size

    def size(self):
        """Return the size of our deque."""
        return self._size

    def peek(self):
        """."""
        return self.tail.data

    def peekleft(self):
        """."""
        return self.head.data

    def __repr__(self):
        """Ensure the print function will run the display."""
        return self.display()
