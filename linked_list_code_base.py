"""Singly linked list creation."""


class Node(object):
    """Creates a node object."""

    def __init__(self, data, next_node):
        """Constructor for the Node object."""
        self.data = data
        self.next_node = next_node


class LinkedList(object):
    """Class for containing object called LinkedList."""

    def __init__(self, iterable=()):
        """Constructor for the Linked List object."""
        self.head = None
        self._counter = 0
        if isinstance(iterable, (str, tuple, list)):
            for item in iterable:
                self.push(item)

    def push(self, val):
        """Add a new value to the head of the linked list."""
        new_head = Node(val, self.head)
        self.head = new_head
        self._counter += 1

    def pop(self):
        """Remove & return the value of the head of the Linked List."""
        if not self.head:
            raise IndexError("The list is empty, so there's nothing to pop.")
        output = self.head.data
        self.head = self.head.next_node
        self._counter -= 1
        return output

    def size(self):
        """Return the size of our list."""
        return self._counter

    def __len__(self):
        """Work with len() function to find length of linked list."""
        return self._counter

    def search(self, val):
        """Search for a given node value and returns it."""
        curr = self.head
        if not curr:
            return "The list is empty."
        while curr:
            if curr.data == val:
                return curr
            curr = curr.next_node
        return

    def remove(self, val):
        """Search for a given value and remove it from the linked list."""
        # search for val.  remove node returned by search func.
        curr = self.head
        while curr:
            if curr.next_node.data == val:
                curr.next_node = curr.next_node.next_node
                self._counter -= 1
                return
            curr = curr.next_node

    def display(self):
        """Will return a unicode string representing the list as if it were a Python tuple literal: “(12, ‘sam’, 37, ‘tango’)”"""
        curr = self.head
        the_thing = "("
        while curr:
            the_thing += str(curr.data) + ", "
            curr = curr.next_node
        the_thing = the_thing[:-2]
        the_thing += ")"
        return the_thing


    def __repr__(self):
        return self.display()