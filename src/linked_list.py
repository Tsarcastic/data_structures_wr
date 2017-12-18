"""Singly linked list creation."""


class Node(object):
    """Creates a node object."""

    def __init__(self, data, next_node):
        """Constructor for the Node object."""
        self.data = data
        self.next = next_node


class LinkedList(object):
    """Class for containing object called LinkedList."""

    def __init__(self, iterable=()):
        """Constructor for the Linked List object."""
        self.head = None
        self._counter = 0
        if hasattr(iterable, '__iter__') or isinstance(iterable, str):
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
        self.head = self.head.next
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
            return
        while curr:
            if curr.data == val:
                return curr
            curr = curr.next
        raise ValueError("Value not found.")

    def remove(self, val):
        """Search for a given value and remove it from the linked list."""
        curr = self.head
        while curr:
            if curr.next == val:
                curr.next = curr.next.next
                self._counter -= 1
                return
            curr = curr.next

    def display(self):
        """Return a string representing the list."""
        curr = self.head
        if self._counter == 0:
            return "()"
        output = "("
        while curr:
            if isinstance(curr.data, (int, float)):
                output += "{}, ".format(str(curr.data))
            else:
                output += "'{}', ".format(str(curr.data))
            curr = curr.next
        output = output[:-2]
        output += ")"
        return output

    def __repr__(self):
        """Print the list to the screen using built in print()."""
        return self.display()
