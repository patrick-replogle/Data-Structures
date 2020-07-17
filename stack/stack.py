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

   An array is far more efficient at implementing a stack since it can both push and 
   pop in constant time. While a singly linked list can easily push a new value to the 
   list, in order to pop from the end you must also have access to the previous node 
   in order to reset the tail and cut it's link to the removed tail. This requires 
   looping thru the list and also further adding space complexity by storing 
   the current node and previous node in memory while looping.  Therefore popping is 
   a linear action and has an O(n) time complexity, making the array a better choice 
   for a stack.
"""
from singly_linked_list import LinkedList


class Stack:
    # Implementation of a stack using an array for data storage
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        return self.storage.add_to_tail(value)

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_tail()
        else:
            return None

# Implementation of a stack using an array for data storage
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.storage.append(value)
#         self.size += 1
#         return self.storage[len(self.storage) - 1]

#     def pop(self):
#         if self.size > 0:
#             self.size -= 1
#             return self.storage.pop(len(self.storage) - 1)
#         else:
#             return None
