class Stack:

    """ O(1) """
    def __init__(self, max_size=1000):
        self.max_size = max_size
        self.stack = [None] * max_size
        self.top = -1

    """ O(1) """
    def is_empty(self):
        return self.top == -1

    """ O(1) """
    def is_full(self):
        return self.top == self.max_size

    """ O(1) """
    def push(self, data):
        if self.is_full():
            return False
        self.top += 1
        self.stack[self.top] = data
        return True

    """ O(1) """
    def pop(self):
        if self.is_empty():
            return None
        data = self.stack[self.top]
        self.top -= 1
        return data

    """ O(1) """
    def view(self):
        if self.is_empty():
            return None
        return self.stack[self.top]
