"""Create a Queue consisting of Nodes."""


class Node(object):
    """A Node which contains a value."""

    def __init__(self, data, previous):
        """Create a new Node."""
        self.data = data
        self.previous = previous
        self.next_node = None


class Queue(object):
    """A Line of Nodes."""

    def __init__(self):
        """Create an empty queue."""
        self.head = None
        self.tail = None
        self._counter = 0

    def enqueue(self, val):
        """Add a node to the tail of the queue."""
        new_tail = Node(val, self.tail)
        if self.tail is None:
            self.head = new_tail
            self.tail = new_tail
        else:
            self.tail.next_node = new_tail
            self.tail = new_tail
        self._counter += 1


    def dequeue(self):
        """Remove a node from the head of the queue."""
        if not self.head:
            raise IndexError("There is nothing to dequeue.")
        output = self.head.data
        if self.head.next_node:
            self.head.next_node.previous = None
            self.head = self.head.next_node
            self._counter -= 1
        else:
            self.head.next_node.previous = None
        return output

    def peek(self):
        """Access the value of the head of the queue."""
        return self.head.data

    def size(self):
        """Return the size of the queue."""
        return self._counter

    def __len__(self):
        """Work with len() function to find length of linked list."""
        return self._counter