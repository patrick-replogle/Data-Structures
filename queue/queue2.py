class Queue:
    # Implementation of a queue using an array
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        self.storage.append(value)
        return self.storage[len(self.storage) - 1]

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.pop(0)
        else:
            return None

    def peek(self):
        if self.size > 0:
            return self.storage[0]
        else:
            return None
