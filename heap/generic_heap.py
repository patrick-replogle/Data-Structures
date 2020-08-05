import math


class Heap:
    def __init__(self, comparator=None):
        self.storage = []
        self.comparator = comparator

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        removed_node = None
        if self.get_size() == 1:
            removed_node = self.storage.pop()
        elif self.get_size() >= 2:
            removed_node = self.storage[0]
            last_node = self.storage.pop()
            self.storage[0] = last_node
            self._sift_down(0)
        return removed_node

    def get_priority(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        if self.comparator is None:
            # max heap bubble up
            current_node = self.storage[index]
            while index > 0:
                parent_index = math.floor((index - 1) / 2)
                parent_node = self.storage[parent_index]
                if self.storage[index] <= parent_node:
                    break
                self.storage[parent_index] = current_node
                self.storage[index] = parent_node
                index = parent_index
        else:
            # min heap bubble up
            current_node = self.storage[index]
            while index > 0:
                parent_index = math.floor((index - 1) / 2)
                parent_node = self.storage[parent_index]
                if self.storage[index] >= parent_node:
                    break
                self.storage[parent_index] = current_node
                self.storage[index] = parent_node
                index = parent_index

    def _sift_down(self, index):
        if self.comparator is None:
            # max heap sift down
            max_index = index
            left_index = 2 * index + 1
            right_index = 2 * index + 2

            if left_index < self.get_size():
                if self.storage[left_index] > self.storage[max_index]:
                    max_index = left_index

            if right_index < self.get_size():
                if self.storage[right_index] > self.storage[max_index]:
                    max_index = right_index

            if max_index != index:
                temp = self.storage[index]
                self.storage[index] = self.storage[max_index]
                self.storage[max_index] = temp
                self._sift_down(max_index)
        else:
            # min heap sift down
            min_index = index
            left_index = 2 * index + 1
            right_index = 2 * index + 2

            if left_index < self.get_size():
                if self.storage[left_index] < self.storage[min_index]:
                    min_index = left_index

            if right_index < self.get_size():
                if self.storage[right_index] < self.storage[min_index]:
                    min_index = right_index

            if index != min_index:
                temp = self.storage[index]
                self.storage[index] = self.storage[min_index]
                self.storage[min_index] = temp
                self._sift_down(min_index)
