# Data-Structures




------------------
## Linked-List
-------------------
### Push
The *push()* method pushes a new Node onto a list. This list uses FILO, which is First In Last Out.
The Time Complexity for this method is O(1). Time is constant because you do not have to iterate through the list.

### Pop
The *pop()* method removes a node off the top of the list. This list uses FILO, which is First In Last Out.
The Time Complexity for this method is O(1). Time is constant because you do not have to iterate through the list.

### Size
The *size()* method returns the value of the counter attribute of the list, which is tracked as the list is populated/depopulated.
Time Complexity for size is O(1), since the value is tracked as an attribute, all we have to do is access the attribute.

### __len__
The *__len__* method allows us to use the standard len() method and we re-map it to return the value returned by the size() method.

### Search
The *search(value)* method takes in a value as a parameter, and traverses the list checking each node to see if it has that value.  If the value is found, the node containing it is returned.
Time Complexity of this function is O(n).  This is because in the worst-case-scenario the function will run a number of times equal to the length of the list, so the length of the list is the deciding factor on how long this runs.  Worst-case-scenarios would be a. if the list didn't contain the value, and b. if the value belonged to the last node in the list.

### Remove
The *remove(val)* method takes in a value as a parameter.  It traverses the list to find that value, and if it is found, the node containing it is removed from the list.
Time Complexity of this function is O(n).  This is because in the worst-case-scenario the function will run a number of times equal to the length of the list, so the length of the list is the deciding factor on how long this runs.  Worst-case-scenarios would be a.) if the list didn't contain the value, and b.) if the value belonged to the last node in the list.

### Display
The *display()* method traverses the list and builds a tuple-like string containing all the values in the list, and returns that string.
Time Complexity of this function is O(n).  This is because in the worst-case-scenario the function will run a number of times equal to the length of the list, so the length of the list is the deciding factor on how long this runs.  Worst-case-scenarios would be a. if the list didn't contain the value, and b. if the value belonged to the last node in the list.

------------------
## Stack
-------------------
### Push
The *push()* method pushes a new Node into a stack. This stack uses FILO, which is First In Last Out.
The Time Complexity for this method is 0(1). Time is constant because you do not have to iterate through the stack.

### Pop
The *pop()* method removes a node off the top of the stack. This stack uses FILO, which is First In Last Out.
The Time Complexity for this method is 0(1). Time is constant because you do not have to iterate through the stack.

### Size
The *size()* method returns the value of the counter attribute of the stack, which is tracked as the stack is populated/depopulated.
Time Complexity for size is O(1), since the value is tracked as an attribute, all we have to do is access the attribute.

### __len__
The *__len__* method allows us to use the standard len() method and we re-map it to return the value returned by the size() method.

------------------
## Double-Linked-List
-------------------
### Push
The *push(val)* method pushes a new Node onto a list.
The Time Complexity for this method is O(1). Time is constant because you do not have to iterate through the list.

###Append
The *append(val)* method adds a new value to the end of the list.
The Time Complexity for this method is O(1). Time is constant because you do not have to iterate through the list.

### Pop
The *pop()* method removes a Node off the top of the list, and returns its value.
The Time Complexity for this method is O(1). Time is constant because you do not have to iterate through the list.

### Shift
The *shift()* method removes the last node from the list and returns its value.
The Time Complexity for this method is O(1). Time is constant because you do not have to iterate through the list.

### Remove
The *remove(val)* method takes in a value as a parameter.  It traverses the list to find that value, and if it is found, the node containing it is removed from the list.
Time Complexity of this function is O(n).  This is because in the worst-case-scenario the function will run a number of times equal to the length of the list, so the length of the list is the deciding factor on how long this runs.  Worst-case-scenarios would be a.) if the list didn't contain the value, and b.) if the value belonged to the last node in the list.

### Size
The *size()* method returns the value of the counter attribute of the list, which is tracked as the list is populated/depopulated.
Time Complexity for size is O(1), since the value is tracked as an attribute, all we have to do is access the attribute.

### __len__
The *__len__* method allows us to use the standard len() method and we re-map it to return the value returned by the size() method.

### Search
The *search(value)* method takes in a value as a parameter, and traverses the list checking each node to see if it has that value.  If the value is found, the node containing it is returned.
Time Complexity of this function is O(n).  This is because in the worst-case-scenario the function will run a number of times equal to the length of the list, so the length of the list is the deciding factor on how long this runs.  Worst-case-scenarios would be a. if the list didn't contain the value, and b. if the value belonged to the last node in the list.


### Display
The *display()* method traverses the list and builds a tuple-like string containing all the values in the list, and returns that string.
Time Complexity of this function is O(n).  This is because in the worst-case-scenario the function will run a number of times equal to the length of the list, so the length of the list is the deciding factor on how long this runs.  Worst-case-scenarios would be a. if the list didn't contain the value, and b. if the value belonged to the last node in the list.


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