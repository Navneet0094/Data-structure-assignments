class DynamicArray:
    def __init__(self, initial_capacity=10):
        self.capacity = initial_capacity
        self.array = [None] * self.capacity
        self.size = 0

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        return self.array[index]

    def __setitem__(self, index, value):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        self.array[index] = value

    def append(self, value):
        if self.size == self.capacity:
            self._resize()
        self.array[self.size] = value
        self.size += 1

    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        if self.size == self.capacity:
            self._resize()
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = value
        self.size += 1

    def delete(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]
        self.size -= 1

    def _resize(self):
        self.capacity *= 2
        new_array = [None] * self.capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

    def __str__(self):
        return str(self.array[:self.size])
    
arr = DynamicArray()
arr.append(1)
arr.append(2)
arr.append(3)
print(arr)  # [1, 2, 3]

arr.insert(1, 4)
print(arr)  # [1, 4, 2, 3]

arr.delete(2)
print(arr)  # [1, 4, 3]

arr.append(5)
print(arr)  # [1, 4, 3, 5]

