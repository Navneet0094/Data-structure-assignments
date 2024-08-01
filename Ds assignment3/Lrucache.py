class Node:
    def __init__(self, key, value):  # initialisation a node with key value
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:   # initialisation lru cache
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):        # getting value of a key from cache
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1
    
    def _add(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove(self, node):   # removig a node
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def put(self, key, value):    # putting a keyvalue pair
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self._add(node)
        self.cache[key] = node
        self.size += 1
        if self.size > self.capacity:
            node = self._pop()
            del self.cache[node.key]
            self.size -= 1

    def _pop(self):
        node = self.tail.prev
        self._remove(node)
        return node

if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print("Get 1:", cache.get(1)) 
    cache.put(3, 3)
    print("Get 2:", cache.get(2)) 
    cache.put(4, 4)
    print("Get 1:", cache.get(1))
    print("Get 3:", cache.get(3))
    print("Get 4:", cache.get(4))