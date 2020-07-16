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


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


class Queue:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.size = 0

    def __len__(self):
        return self.size

    def enqueue(self, value):
        new_node = Node(value)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node
        self.size += 1
        return f"{self.tail.value} is #{self.size} in line"

    def dequeue(self):
        if self.size == 0:
            return None

        removed_node = self.head
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = removed_node.next_node
            removed_node.next_node = None
        self.size -= 1
        return removed_node.value

    def peek(self):
        return self.head.value


queue = Queue()
queue.enqueue(1)
print(queue.dequeue())
print(queue.size)
