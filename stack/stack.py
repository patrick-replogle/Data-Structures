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
   the current.node and previous node in memory while looping.  Therefore popping is 
   a linear action and has an O(n) time complexity, making the array a better choice 
   for a stack.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None


class Stack:
    # Implementation of a stack using a singly linked list for data storage
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
        return self.tail.value

    def pop(self):
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
print(stack.push(1))
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.pop()
print(stack.peek())
