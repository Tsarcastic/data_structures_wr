"""Singly linked list creation."""


class Node(object):
    """Creates a node object."""

<<<<<<< HEAD
    def __init__(self, data, next, previous="None"):
        """Constructor for the Node object."""
        self.data = data
        self.next = next
=======
    def __init__(self, data, next_n, previous="None"):
        """Constructor for the Node object."""
        self.data = data
        self.next_n = next_n
>>>>>>> 9c30e3643d04c58640bf1bfc57399115ef739245
        self.previous = previous


class DoubleLinkedList(object):
    """Class for containing object called LinkedList."""

    def __init__(self):
        """Constructor for the Linked List object."""
        self.head = None
        self.tail = None
        self._counter = 0

    def push(self, val):
        """Add a new value to the head of the linked list."""
        new_head = Node(val, self.head)
        if self.head is None:
            self.tail = new_head
            self.head = new_head
        else:
            self.head.previous = new_head
            self.head = new_head
        self._counter += 1

    def append(self, val):
        """Add a node to the tail of the queue."""
        new_tail = Node(val, None, self.tail)
        if self.tail is None:
            self.head = new_tail
            self.tail = new_tail
        else:
<<<<<<< HEAD
            self.tail.next = new_tail
=======
            self.tail.next_n = new_tail
>>>>>>> 9c30e3643d04c58640bf1bfc57399115ef739245
            self.tail = new_tail
        self._counter += 1

    def pop(self):
        """Remove & return the value of the head of the Linked List."""
        if not self.head:
            raise IndexError("The list is empty, so there's nothing to pop.")
        output = self.head.data
<<<<<<< HEAD
        self.head.next.previous = None
        self.head = self.head.next
=======
        self.head.next_n.previous = None
        self.head = self.head.next_n
>>>>>>> 9c30e3643d04c58640bf1bfc57399115ef739245
        self._counter -= 1
        return output

    def shift(self):
        """Remove last node from list."""
        if not self.tail:
            raise IndexError("The list is empty, so there's nothing to pop.")
        else:
            temp = self.tail.data
            self.tail = self.tail.previous
<<<<<<< HEAD
            self.tail.next = None
=======
            self.tail.next_n = None
>>>>>>> 9c30e3643d04c58640bf1bfc57399115ef739245
        self._counter -= 1
        return temp

    def size(self):
        """Return the size of our list."""
        return self._counter

    def __len__(self):
        """Work with len() function to find length of linked list."""
        return self._counter

    def search(self, val):
        """Searche for a given node value and returns it."""
        curr = self.head
        while curr.data == val:
            return curr
<<<<<<< HEAD
        curr = curr.next
=======
        curr = curr.next_n
>>>>>>> 9c30e3643d04c58640bf1bfc57399115ef739245

    def remove(self, val):
        """Search for a given node value and remove it from the linked list."""
        curr = self.head
        while curr:
<<<<<<< HEAD
            if curr.next.data == val:
                curr.next = curr.next.next
                curr.next.previous = curr
                self._counter -= 1
                return
            curr = curr.next
        pass

    def display(self):
        u"""Will return a unicode string representing the list as if it were.

        a Python tuple literal: “(12, ‘sam’, 37, ‘tango’)”.
        """
        pass
# make sure print(linked_list) will run the display method
=======
            if curr.next_n.data == val:
                curr.next_n = curr.next_n.next_n
                curr.next_n.previous = curr
                self._counter -= 1
                return
            curr = curr.next_n
        pass

    def display(self):
        """Will return a unicode string representing the list as if it were a Python tuple literal: “(12, ‘sam’, 37, ‘tango’)”"""
        curr = self.head
        the_thing = "("
        while curr:
            the_thing += str(curr.data) + ", "
            curr = curr.next_n
        the_thing = the_thing[:-2]
        the_thing += ")"
        return the_thing

    def __repr__(self):
        """Ensure the print function will run the display"""
        return self.display()
     
>>>>>>> 9c30e3643d04c58640bf1bfc57399115ef739245
