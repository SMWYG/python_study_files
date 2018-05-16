class LinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.head = None

    def add_head(self, value):
        node = self.Node(value)
        node.next = self.head
        self.head = node

    def find(self, value): # 값으로 찾는 것 true/false 반환
        current = self.head
        while current:
            if value == current.value:
                return True
            current = current.next
        return False
    
    def get_at(self, idx): # 인덱스로 값을 찾는 것 true/false 반환
        current = self.head
        count = 0
        while current:
            if idx == count:
                return current.value
            count += 1
            current = current.next
        return None

    def print(self):
        for val in self.traverse(): # for문이 next를 호출해줌 for문은 원래 이터레이터를 받은 것이였다.
            print(val, end='')
        print()
        # current = self.head
        # while current:
        #     print(current.value, end=' -> ' )
        #     current = current.next
        # print(None)

    def traverse(self): # 이터레이터_제너레이터 함수
        current = self.head
        while current:
            yield current.value
            current = current.next


l = LinkedList()
l.add_head(10)
l.add_head(20)
l.add_head(30)

l.print()

print(l.find(50))
print(l.get_at(2))
