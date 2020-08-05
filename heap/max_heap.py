import math


class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        # add value to the end of the list
        self.storage.append(value)
        # call bubble up to find the correct placement for the value in the heap
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        max_node = None
        if self.get_size() == 1:
            max_node = self.storage.pop()
        elif self.get_size() >= 2:
            # remove largest node
            max_node = self.storage[0]
            # remove the min (last) node and move it to the front of the array
            last_node = self.storage.pop()
            self.storage[0] = last_node
            # call recursive function sift down to re-balance the heap
            self._sift_down(0)
        return max_node

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        # store current value in variable. starts as last value in array
        current_node = self.storage[index]
        while index > 0:
            # store the parent value of the current value
            parent_index = math.floor((index-1)/2)
            parent_node = self.storage[parent_index]
            # current value is less than parent value => break out of loop
            if current_node <= parent_node:
                break
            # else swap the parent and current values
            self.storage[parent_index] = current_node
            self.storage[index] = parent_node
            # move the index to the parent index to start the loop over
            # to compare the new current value to it's parent value
            index = parent_index

    def _sift_down(self, index):
        # index will start at 0 the first call
        max_index = index
        # store left child and right child index's of the parent index
        left_index = 2 * index + 1
        right_index = 2 * index + 2
        # make sure the left child exists
        if left_index < self.get_size():
            if self.storage[left_index] > self.storage[max_index]:
                max_index = left_index
        # make sure the left child exists
        if right_index < self.get_size():
            # compare storage
            if self.storage[right_index] > self.storage[max_index]:
                max_index = right_index
        # check if max index is no longed the passed in index and
        if max_index != index:
            # if max_index has changed, swap the values
            temp = self.storage[index]
            self.storage[index] = self.storage[max_index]
            self.storage[max_index] = temp
            # lastly, recursivly call sift down to re-balance entire list
            self._sift_down(max_index)
