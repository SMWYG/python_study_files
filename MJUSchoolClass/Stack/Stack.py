class Stack:
    def __init__(self):
        self.list = []

    def is_empty(self):
        return not self.list

    def push(self, item):
        self.list.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.list.pop()

    def peek(self):
        return self.list[-1]


# s = Stack()
# print(s.is_empty())
# s.push(1)
# s.push(2)
# print(s.peek())
# print(s.pop())
# print(s.pop())
# print(s.pop())
