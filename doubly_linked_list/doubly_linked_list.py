"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
    
    def set_next(self, value):
        self.next = value
            
    def get_next(self):
        return self.next.get_value()
    
    def get_value(self):
        return self.value
    
    def set_prev(self, value):
        self.prev = value
    
    def get_prev(self):
        return self.prev.get_value()
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        
        new_node = ListNode(value)
        self.length += 1

        # check if empty
        if self.head is None and self.tail is None:
           self.head = new_node
           self.tail = new_node
        # the list must have a node in it
        else:
            new_node.set_next(self.head)
            self.head.set_prev(new_node)
            self.head = new_node

        
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        pass
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1

        # check if empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        # the list must have a node in it
        else:
            new_node.set_prev(self.tail)
            self.tail.set_next(new_node)
            self.tail = new_node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        pass
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        pass
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        pass

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass

dll = DoublyLinkedList()

dll.add_to_head(1)
dll.add_to_head(2)
dll.add_to_tail(3)

print(dll.head.get_value())
print(dll.head.get_next())
print(dll.tail.get_value())
print(dll.tail.get_prev())