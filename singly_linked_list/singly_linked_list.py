class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def add_to_head(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        if self.length == 0:
            self.tail = new_node
        self.length += 1
    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
        else:
            self.tail.set_next(new_node)
        self.tail = new_node
        self.length += 1
    def remove_head(self):
        if self.head is None:
            return None
        elif self.head == self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            return value

        else:
            value = self.head.get_value()
            self.head = self.head.get_next()
            self.length -= 1
            return value

    def remove_tail(self):
        if self.head is None:
            return None
        elif self.head == self.tail:
            value = self.tail.get_value()

            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else:
            value = self.tail.get_value()
            self.tail = None
            self.length -= 1
            return value

