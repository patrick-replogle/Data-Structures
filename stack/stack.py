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


class Stack:
    # Implementation of a stack using an array for data storage
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        pass

    def push(self, value):
        pass

    def pop(self):
        pass

    def clear(self):
        pass

    def peek(self):
        pass


# class Stack:
#     # Implementation of a stack using an array for data storage
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
