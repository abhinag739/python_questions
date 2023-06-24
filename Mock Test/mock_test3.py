"""Implement a stack using a list in Python. Include the necessary methods such as push, pop, and isEmpty."""

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Stack is already empty")

    def is_empty(self):
        return len(self.stack) == 0



stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print(stack.pop())  # Output: 30
print(stack.pop())  # Output: 20

print(stack.is_empty())  # Output: False

print(stack.pop())  # Output: 10

print(stack.is_empty())  # Output: True