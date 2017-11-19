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
## Queue
-------------------
The Queue structure is a FIFO structure which is First In First Out. 

### Enqueue
The *enqueue(val)* method adds a new value to the end of the queue.
The Time Complexity for this method is O(1). Time is constant because you do not have to iterate through the queue.

### Dequeue
The *dequeue()* method removes a Node off the top of the queue, and returns its value.
The Time Complexity for this method is O(1). Time is constant because you do not have to iterate through the queue.

### Peek
The *peek()* method looks returns the value of the next node in the list, without removing that node.
The Time Complexity for this method is O(1). Time is constant because you do not have to iterate through the queue.

### Size
The *size()* method returns the value of the counter attribute of the queue, which is tracked as the queue is populated/depopulated.
Time Complexity for size is O(1), since the value is tracked as an attribute, all we have to do is access the attribute.

### __len__
The *__len__* method allows us to use the standard len() method and we re-map it to return the value returned by the size() method.
