"""Create a Queue consisting of Nodes."""


class Node(object):
        """A Node which contains a value."""

  
    def __init__(self, data, next):
        """Creates a new Node."""
        self.data = data
        self.next = next 
        self.previous = None

class Queue(object):


    def __init__(self):
        self.head = None
        self.tail = None
        self._counter = 0


    def enqueue(self, val):
        new_head = Node(val, self.head)
        if self.head is None:
            self.tail = new_head
            self.head = new_head
        else:
            
            self.head = new_head
        self._counter += 1


    def dequeue():
        if not self.tail:
            raise IndexError("The queue is currently empty.")
        else:
            temp = self.tail.data


