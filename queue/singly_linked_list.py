class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.size = 0

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node
        self.size += 1

    def remove_tail(self):
        if self.head is None and self.tail is None:
            return None

        elif self.size == 1:
            removed_node = self.tail
            self.head = None
            self.tail = None
            self.size = 0
            return removed_node.value

        else:
            previous_node = None
            current_node = self.head
            while(current_node):
                if current_node.value == self.tail.value:
                    self.tail = previous_node
                    previous_node.next_node = None
                    self.size -= 1
                    return current_node.value
                else:
                    previous_node = current_node
                    current_node = current_node.next_node

    def add_to_head(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node
        self.size += 1

    def remove_head(self):
        if self.head is None and self.tail is None:
            return None

        removed_node = self.head
        if self.head.next_node is None:
            self.head = None
            self.tail = None
        else:
            self.head = removed_node.next_node
            removed_node.next_node = None
        self.size -= 1
        return removed_node.value

    def contains(self, value):
        current_node = self.head

        while current_node:
            if current_node.value == value:
                return True
            else:
                current_node = current_node.next_node
        return False

    def get_max(self):
        if self.head is None:
            return None

        max_value = 0
        current_node = self.head

        while current_node:
            if current_node.value > max_value:
                max_value = current_node.value
            current_node = current_node.next_node

        return max_value
