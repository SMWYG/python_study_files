class SinglyLinkedList:
    # insert_head : O(1)
    # insert_tail : O(n)
    # delete_head : O(1)
    # delete_tail : O(n)
    # insert_pos : O(n)
    # delete_pos : O(n)
    # select_pos : O(n)
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.head = None  # head만 알고 있는 리스트이므로 head만 변수로 존재한다.

    def insert_head(self, value): # O(1)
        node = self.Node(value)
        node.next = self.head
        self.head = node

    def insert_tail(self, value): # O(n)
        node = self.Node(value)
        if (self.head == None):
            self.head = node
        else:
            current = self.head
            while (current):
                if current.next:
                    current = current.next
                else:
                    current.next = node
                    break

    def delete_head(self): # O(1)
        if (self.head == None):
            return print('Warning!! : No value, please insert the value')
        node = self.head
        self.head = node.next

    def delete_tail(self): # O(n)
        if (self.head == None):
            return print('Warning!! : No value, please insert the value')
        elif (self.head.next == None):
            self.head = None
        else:
            current = self.head.next
            pre = self.head
            while (current):
                if current.next:
                    pre = current
                    current = current.next
                else:
                    pre.next = None
                    break

    def insert_middle(self, index, value): # O(n)
        node = self.Node(value)
        if (self.head == None):
            self.head = node
        elif (self.head.next == None and index == 0) or (index == 0):
            node.next = self.head
            self.head = node
        else:
            current = self.head
            i = 0
            while(current):
                if (index-1) == i:
                    node.next = current.next
                    current.next = node
                    return
                current = current.next
                i += 1
            return print('Warning!! : index out of range!')

    def delete_middle(self, index): # O(n)
        if self.head == None:
            return print('Warning!! : No value, please insert the value')
        elif (self.head.next == None) and (index == 0):
            self.head = None
        elif index == 0:
            self.head = self.head.next
        else:
            current = self.head
            i = 0
            while current:
                if (index-1) == i:
                    if current.next.next:
                        current.next = current.next.next
                        return
                    else:
                        current.next = None
                        return
                current = current.next
                i += 1
            return print('Warning!! : index out of range!')

    def select(self, index): # O(n)
        if self.head == None:
            return print('Warning!! : No value, please insert the value')
        current = self.head
        i = 0
        while(current):
            if index == i:
                return current.value
            current = current.next
            i += 1
        return print('Warning!! : index out of range!')





list = SinglyLinkedList()

list.insert_head(3)
list.insert_head(2)
list.insert_head(1)
p = list.head
# print(p.next.next.value)
while p:
    print(p.value, end=' ')
    p = p.next
print()

