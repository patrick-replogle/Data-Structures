class Stack:
    # Implementation of a stack using an array for data storage
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.append(value)
        self.size += 1
        return self.storage[len(self.storage) - 1]

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.pop(len(self.storage) - 1)
        else:
            return None

    def clear(self):
        self.size = 0
        self.storage.clear()
        return self.storage

    def peek(self):
        if self.size > 0:
            return self.storage[len(self.storage) - 1]
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
