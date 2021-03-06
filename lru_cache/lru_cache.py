from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.limit = limit
        self.cache = DoublyLinkedList()
        self.dict = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        if key in self.dict:
            value = self.dict[key]
            self.cache.move_to_end({key: value})
            return value
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        if self.cache.length == 0:
            self.cache.add_to_head({key: value})
            self.dict[key] = value

        elif key in self.dict:
            self.cache.delete({key: value})
            self.cache.add_to_tail({key: value})
            self.dict[key] = value

        elif self.cache.length < self.limit and not key in self.dict:
            self.cache.add_to_tail({key: value})
            self.dict[key] = value

        elif self.cache.length >= self.limit:
            deleted = self.cache.remove_from_head()
            deleted_key = [*deleted][0]
            del self.dict[deleted_key]
            self.cache.add_to_tail({key: value})
            self.dict[key] = value
