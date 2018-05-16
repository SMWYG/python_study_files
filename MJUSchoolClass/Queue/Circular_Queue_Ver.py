'''
add : O(1)
delete : O(1)
isFull : O(1)
isEmpty : O(1)
'''
class Queue:
    def __init__(self, max):
        self.queue = [None]*(max+1)
        self.max = max
        self.front = 0
        self.rear = 0
        print(self.queue)

    def add(self, value): # O(1)
        if self.isFull():
            return print('Full...')
        else:
            self.queue[self.rear%self.max] = value
            self.rear += 1

    def delete(self): # O(1)
        if self.isEmpty():
            return print('Empty...')
        else:
            print(self.queue[self.front%self.max])
            self.front += 1

    def isFull(self): # O(1)
        return True if (self.rear%(self.max)) == (self.front%(self.max))\
                       and self.queue[self.front%(self.max-1)] is not None else False

    def isEmpty(self): # O(1)
        return self.front == self.rear


queue = Queue(3)
queue.add(1)
queue.add(2)
queue.add(3)






