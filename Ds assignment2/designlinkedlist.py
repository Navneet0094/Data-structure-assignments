class MyLinkedList:
    class Node:
        def __init__(self, val):
            self.val = val
            self.next = None

    def __init__(self):
        self.head = None
        self.length = 0

    def get(self, index):
        if index >= self.length:
            return -1
        counter = 0
        temp = self.head
        while counter < index:
            counter += 1
            temp = temp.next
        return temp.val

    def add_at_head(self, val):
        new_node = self.Node(val)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def add_at_tail(self, val):
        if self.head is None:
            self.add_at_head(val)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            new_node = self.Node(val)
            temp.next = new_node
            self.length += 1

    def add_at_index(self, index, val):
        if index > self.length:
            return
        if index == 0:
            self.add_at_head(val)
        else:
            counter = 1
            temp = self.head
            while counter < index:
                temp = temp.next
                counter += 1
            new_node = self.Node(val)
            next_node = temp.next
            temp.next = new_node
            new_node.next = next_node
            self.length += 1

    def delete_at_index(self, index):
        if index >= self.length:
            return
        if index == 0:
            self.head = self.head.next
            self.length -= 1
        else:
            counter = 1
            temp = self.head
            while counter < index:
                counter += 1
                temp = temp.next
            temp.next = temp.next.next
            self.length -= 1