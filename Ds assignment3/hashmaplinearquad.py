class LinearProbingHashMap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.keys = [None] * capacity
        self.values = [None] * capacity

    def _hash(self, key):
        return hash(key) % self.capacity

    def find(self, key):
        index = self._hash(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return True
            index = (index + 1) % self.capacity
        return False

    def insert(self, key, value):
        if self.size == self.capacity:
            raise Exception("Hashmap is full")
        index = self._hash(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = value
                return
            index = (index + 1) % self.capacity
        self.keys[index] = key
        self.values[index] = value
        self.size += 1

    def remove(self, key):
        index = self._hash(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.keys[index] = None
                self.values[index] = None
                self.size -= 1
                return
            index = (index + 1) % self.capacity

# Example usage:
hashmap = LinearProbingHashMap(10)
hashmap.insert("roll no 1", 123)
hashmap.insert("roll no 2", 123)
print(hashmap.find("roll no 1"))  
hashmap.remove("roll no 1")
print(hashmap.find("navneet"))  
hashmap.remove("roll no 2")
print(hashmap.find("roll no 2"))

