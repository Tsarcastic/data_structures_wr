# Data-Structures
-------------------
## Stack
-------------------
### Push
The *push()* method pushes a new Node into a stack. This stack uses FILO, which is First In Last Out.
The Time Complexity for this method is 0(1). Time is constant because you do not have to iterate through the list.

### Pop
The *pop()* method removes a new Node off the top of the stack. This stack uses FILO, which is First In Last Out.
The Time Complexity for this method is 0(1). Time is constant because you do not have to iterate through the list.

-------------------
### Priority Queue
-------------------

###Insert
The *insert() method adds a node to the tail of the queue.
The Time Complexity for this method is O(1) because we don't need to iterate through the structure

###Pop
The *pop() method removes the node with the highest priority, or if all priorities are equal it removes the item at the head of the list.
The Time Complexity for this method is O(N) because we used a double linked list instead of a binary heap so it has to iterate through each item.

###Peek
The *peek() method accesses the value of the head of the queue.
The Time Complexity for this method is O(1) because we don't need to iterate through the list.

###Size
The *size() method returns the size of the queue
The Time Complexity for this method is O(1) because it just needs to access an attribute.

