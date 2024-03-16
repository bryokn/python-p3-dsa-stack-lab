class Stack:

    def __init__(self, items = [], limit = 100):
        #pass
        if items is None:
            self.items = []
        else:
            self.items = items
        self.limit = limit

    def isEmpty(self):
        #pass
        return len(self.items) == 0

    def push(self, item):
        #pass
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            raise ValueError("Stack is full")

    def pop(self):
        #pass
        if not self.isEmpty():
            return self.items.pop()
        else:
            raise IndexError("Pop from empty stack")

    def peek(self):
        #pass
        if not self.isEmpty():
            return self.items[-1]
        else:
            return None
    
    def size(self):
        #pass
        return len(self.items)

    def full(self):
        #pass
        return len(self.items) == self.limit

    def search(self, target):
        #pass
        if target in self.items:
            return len(self.items) - self.items.index(target) - 1
        else:
            return -1
