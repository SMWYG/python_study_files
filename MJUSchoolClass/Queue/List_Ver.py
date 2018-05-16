'''
add : O(1)
delete : O(n)
isFull : O(1)
isEmpty : O(1)
'''
class Queue:
    def __init__(self):
        self.queue = []

    def add(self, value): # O(1)
        self.queue.append(value)

    def delete(self): # O(n)
        print(self.queue[0])
        del self.queue[0]

    # def isFull(self):
    # 리스트는 immutable 하기 때문에 길이가 계속 늘어날 수 있으므로 일단 기다려 보자 이건 max를 따로 주면 되긴 함

    def isEmpty(self):
        return not self.queue


queue = Queue()
queue.add(3)
queue.add(2)
queue.add(1)
queue.delete()
queue.delete()
queue.delete()
print(queue.isEmpty())

