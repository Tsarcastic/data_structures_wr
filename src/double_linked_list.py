"""Double linked list creation."""


class Node(object):
    """Creates a node object."""

    def __init__(self, data, next_node, previous=None):
        """Constructor for the Node object."""
        self.data = data
        self.next_node = next_node
        self.previous = previous


class DoubleLinkedList(object):
    """Class for a Doubly Linked List."""

    def __init__(self):
        """Constructor for the DLL object."""
        self.head = None
        self.tail = None
        self._counter = 0

    def push(self, val):
        """Add a new value to the head of the DLL."""
        new_head = Node(val, self.head)
        if self.head is None:
            self.tail = new_head
            self.head = new_head
        else:
            self.head.previous = new_head
            self.head = new_head
        self._counter += 1

    def append(self, val):
        """Add a node to the tail of the DLL."""
        new_tail = Node(val, None, self.tail)
        if self.tail is None:
            self.head = new_tail
            self.tail = new_tail
        else:
            self.tail.next_node = new_tail
            self.tail = new_tail
        self._counter += 1

    def pop(self):
        """Remove & return the value of the head of the DLL."""
        if not self.head:
            raise IndexError("The list is empty, so there's nothing to pop.")
        elif self.head == self.tail:
            output = self.head
            self.head = None
            self.tail = None
            self._counter -= 1
            return output.data
        else:
            output = self.head.data
            self.head.next_node.previous = None
            self.head = self.head.next_node
            self._counter -= 1
            return output

    def shift(self):
        """Remove last node from DLL."""
        if not self.tail:
            raise IndexError("The list is empty, so there's nothing to pop.")
        elif self.head == self.tail:
            output = self.head
            self.tail = None
            self.head = None
            self._counter -= 1
            return output
        else:
            temp = self.tail.data
            self.tail = self.tail.previous
            self.tail.next_node = None
            self._counter -= 1
            return temp

    def size(self):
        """Return the size of our DLL."""
        return self._counter

    def __len__(self):
        """Work with len() function to find length of linked list."""
        return self._counter

    def remove(self, val):
        """Search for a given node value and remove it from the linked list."""
        curr = self.head
        if not curr:
            raise Exception('The list is empty.')
        elif self.head == self.tail and self.head.data == val:
            self.head = None
            self.tail = None
            self._counter -= 1
            print('That item has been removed. The list is now empty.')
        elif self.head.data == val:
            self.head = self.head.next_node
            self.head.previous = None
            self._counter -= 1
            print('The item has been removed')
        elif self.tail.data == val:
            self.tail = self.tail.previous
            self.tail.next = None
            self._counter -= 1
            print('The item has been removed.')
        while curr:
            if curr.next_node.data == val:
                curr.next_node = curr.next_node.next_node
                curr.next_node.previous = curr
                self._counter -= 1
                return
            curr = curr.next_node

    def display(self):
        """Will return a unicode string representing the list as if it were a Python tuple literal: “(12, ‘sam’, 37, ‘tango’)."""
        if self._counter == 0:
            raise Exception('The list is empty.')
        curr = self.head
        the_thing = "("
        while curr:
            the_thing += str(curr.data) + ", "
            curr = curr.next_node
        the_thing = the_thing[:-2]
        the_thing += ")"
        return the_thing

    def __repr__(self):
        """Ensure the print function will run the display."""
        return self.display()
