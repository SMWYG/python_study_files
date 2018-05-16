class DoublyLikedList:
    # insert_head : O(1)
    # insert_tail : O(1)
    # delete_head : O(1)
    # delete_tail : O(1)
    # insert_pos : O(n)
    # delete_pos : O(n)
    # select_pos : O(n)
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None
            self.prev = None # 이중연결리스트이므로 prev 변수도 가짐

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_head(self, value): # O(1)
        node = self.Node(value)
        if (self.head == None) and (self.tail == None):
           self.head = node
           self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def insert_tail(self, value): # O(1)
        node = self.Node(value)
        if (self.head == None) and (self.tail == None):
           self.head = node
           self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    def delete_head(self): # O(1)
        if self.head == None:
            return print('Warning!! : No value, please insert the value')
        elif self.head.next == None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def delete_tail(self): # O(1)
        if self.head == None:
            return print('Warning!! : No value, please insert the value')
        elif self.head.next == None:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    # def insert_middle(self, index, value):
    #     node = self.Node(value)



list = DoublyLikedList()
list.insert_head(5)
list.insert_head(3)
list.insert_tail(7)
list.insert_tail(9)

current = list.head
while current:
    print(current.value, end=' ')
    current = current.next