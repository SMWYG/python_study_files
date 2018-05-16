'''
add : O(1)
delete : O(1)
isFull : O(1)
isEmpty : O(1)
'''
class Queue:
    class Node:
        def __init__(self, value):
            self.value : value
            self.next : None

    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value): # O(1)
        new_node = self.Node(value)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def delete(self): # O(1)
        if self.isEmpty():
            return
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

    def isEmpty(self): # O(1)
        return self.head == None and self.tail == None


queue = Queue()
queue.add(3)
queue.add(2)
queue.add(1)
queue.delete()
queue.delete()
queue.delete()
print(queue.isEmpty())


