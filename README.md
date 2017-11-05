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

-------------------
### Deque
-------------------



-------------------
### Bin Heap
-------------------



-------------------
### Priority Queue
-------------------


-------------------
### Graph
The graph consists of a number of nodes and a list of the links between these nodes.
-------------------
##  Nodes
The nodes() method returns a list of all the nodes in the graph.
The time complexity is O(N) because the size directly affects the time.

## Edges
The edges() method returns a list of all the edges in the graph.
The time complexity is O(N) because the size directly affects the time.

## Add_node
The add_node(val) method adds a node to the graph.
The time complexity is O(1) because it does not iterate through the graph.

## Add_edge
The add_edge(val1, val2) method adds an edge between two nodes.
The time complexity is O(1) because it does not iterate through the graph.

## Del_node
The del_node(val) method deletes a node containing a value from the graph.
The time complexity is O(N) because it needs to iterate through the list of nodes.

## Del_edge
The del_edge(val1, val2) method deletes an edge between two nodes.
The time complexity is O(N) because it needs to iterate through the list of edges.

## Has_node
The has_node(val) method checks if a node with that value exists in the graph.
The time complexity is O(N) because it needs to iterate through the list of nodes.

## Neighbors
The neighbors(val) method returns a list of all the nodes connected to a specific node.
The time complexity is O(N) because it needs to iterate through the dictionary of edges.

## Adjacent
The adjacent(val1, val2) method returns true if an edge exists between two nodes or false if it does not.
The time complexity is O(N) because it needs to iterate through the dictionary of edges.

-------------------
## Deque
-------------------
The Deque structure is a list that can add or remove from either the head or the tail.

### Append
The *append(val)* method adds a new value to the end of the deque.
The Time Complexity for this method is O(1). Time is constant because you do not have to iterate through the deque.

### Appendleft
The *appendleft(val)* method adds a new value to the end of the deque.
The Time Complexity for this method is O(1). Time is constant because you do not have to iterate through the deque.

### Pop
The pop() method emoves a value from the end of the deque and returns it (raises an exception if the deque is empty)
The Time Complexity for this method is O(1). Time is constant because you do not have to iterate through the deque.

### Popleft
The popleft method removes a value from the front of the deque and returns it (raises an exception if the deque is empty)
The Time Complexity for this method is O(1). Time is constant because you do not have to iterate through the deque.

###Peek
The peek() method  returns the next value that would be returned by pop but leaves the value in the deque (returns None if the deque is empty)
The Time Complexity for this method is O(1). Time is constant because you do not have to iterate through the deque.

###Peekleft
The peekleft() method returns the next value that would be returned by popleft but leaves the value in the deque (returns None if the deque is empty)
The Time Complexity for this method is O(1). Time is constant because you do not have to iterate through the deque.

###Size
The size() method returns the count of items in the queue (returns 0 if the queue is empty)
The Time Complexity for this method is O(1). Time is constant because you do not have to iterate through the deque.

