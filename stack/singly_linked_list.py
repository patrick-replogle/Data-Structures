class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.size = 0

    def add_to_head(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node
        self.size += 1

    def remove_head(self):
        if self.head is None and self.tail is None:
            return None

        removed_node = self.head
        if self.head.get_next() == None:
            self.head = None
            self.tail = None
        else:
            self.head = removed_node.get_next()
            removed_node.set_next(None)
        self.size -= 1
        return removed_node.get_value()

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
        self.size += 1

    def remove_tail(self):
        if self.head is None and self.tail is None:
            return None

        elif self.size == 1:
            removed_node = self.tail.get_value()
            self.head = None
            self.tail = None
            self.size = 0
            return removed_node

        else:
            previous_node = None
            current_node = self.head
            while current_node:
                if current_node.value == self.tail.value:
                    self.tail = previous_node
                    previous_node.set_next(None)
                    self.size -= 1
                    return current_node.value
                else:
                    previous_node = current_node
                    current_node = current_node.get_next()

    def contains(self, value):
        current_node = self.head

        while current_node:
            if current_node.get_value() == value:
                return True
            else:
                current_node = current_node.get_next()
        return False

    def get_max(self):
        if self.head is None:
            return None

        max_value = 0
        current_node = self.head

        while current_node:
            if current_node.get_value() > max_value:
                max_value = current_node.get_value()
            current_node = current_node.get_next()

        return max_value
