class Node:
    def __init__(self, value, next_node=None):
        # the value that the node is holding 
        self.value = value 
        # reference to the next node in the linked list
        self.next_node = next_node

    # method to get the value of the node 
    def get_value(self):
        return self.value

    # method to get the node's `next_node`
    def get_next(self):
        return self.next_node

    # method to update the node's `next_node` to the input node 
    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_to_tail(self, value):
        # wrap the value in a Node
        new_node = Node(value)
        self.length += 1
        # check if the Linked List is empty 
        if self.head is None and self.tail is None:
            # set head and tail to the new node 
            self.head = new_node
            self.tail = new_node
        # otherwise, the list has at least one node 
        else:
            # update the last node's `next_node` to the new node 
            self.tail.set_next(new_node)
            # update `self.tail` to point the new node we just added 
            self.tail = new_node
    
    def add_to_head(self, value):
        # wrap the value in a Node
        new_node = Node(value)
        self.length += 1
        # check if the Linked List is empty 
        if self.head is None and self.tail is None:
            # set head and tail to the new node 
            self.head = new_node
            self.tail = new_node
        # otherwise, the list has at least one node 
        else:
            # update the last node's `next_node` to the new node 
            self.tail.set_next(new_node)
            # update `self.tail` to point the new node we just added 
            self.tail = new_node

    def remove_tail(self):
        # check if the linked list is empty 
        if self.head is None and self.tail is None:
            return None
        
        # check if the linked list has only one node 
        if self.head == self.tail:
            self.length -= 1
            # store the node we're going to remove's value 
            val = self.head.get_value()
            self.head = None
            self.tail = None
            return val

        # otherwise, the linked list has more than one Node 
        else:
            # store the last Node's value in a nother variable so we can return it 
            val = self.tail.get_value()
            # we need to set `self.tail` to the second-to-last Node
            # the only way we can do this, is by traversing the whole linked list
            # from the beginning 
            
            # starting from the head, we'll traverse down to the second-to-last Node 
            # init another reference to keep track of where we are in the linked 
            # list as we're iterating 
            current = self.head 
            self.length -= 1
            # keep iterating until the node after `current` is the tail
            while current.get_next() != self.tail:
                # keep iterating 
                current = current.get_next()

            # set `self.tail` to `current`
            self.tail = current
            # set the new tail's `next_node` to None
            self.tail.set_next(None) 
            return val

    def remove_head(self):
        # check if the linked list empty 
        if self.head is None and self.tail is None:
            return None
        # check if there is only one linked list node 
        if self.head == self.tail:
            val = self.head.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            return val
        else:
            # store the old head's value that we need to return 
            val = self.head.get_value()
            # set `self.head` to the old head's `next_node`
            self.head = self.head.get_next()
            # return the old_head's value 
            self.length -= 1
            return val

"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
        
#     def __len__(self):
#         return len(self.storage)

#     def enqueue(self, value):
#         self.storage.append(value)
#         self.size += 1

#     def dequeue(self):
#         if not self.__len__() < 1:
#             return self.storage.pop(0)



class Queue:
   def __init__(self):
      self.storage = LinkedList()
   
   def __len__(self):
      return self.storage.length
   
   def enqueue(self, value):
      return self.storage.add_to_head(value)

   def dequeue(self):
      return self.storage.remove_head()

q = Queue()



q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

print(q.dequeue())
print(q.dequeue())




