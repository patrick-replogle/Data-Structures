"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None


# Implementation of a stack using a singly linked list for data storage
class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def push(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node
        self.size += 1

    def pop(self):
        if self.head is None and self.tail is None:
            return None

        if self.size == 1:
            removed_node = self.tail
            self.head = None
            self.tail = None
            self.size = 0
            removed_node.next_node = None
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

    def clear(self):
        if self.size > 0:
            self.head = None
            self.tail = None
        else:
            return None

    def peek(self):
        if self.size > 0:
            return self.tail.value
        else:
            return None


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.pop()
print(stack.peek())

# Implementation of a stack using an array for data storage
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.size += 1
#         return self.storage.append(value)

#     def pop(self):
#         if self.size > 0:
#             self.size -= 1
#             return self.storage.pop(len(self.storage) - 1)
#         else:
#             return None

#     def clear(self):
#         self.size = 0
#         return self.storage.clear()

#     def peek(self):
#         if self.size > 0:
#             return self.storage[len(self.storage) - 1]
#         else:
#             return None
