class SinglyLinkedListHasTail:
    # insert_head : O(1)
    # insert_tail : O(1)
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
        self.head = None
        self.tail = None

    def insert_head(self, value): # O(1)
        node = self.Node(value)
        if (self.head == None) and (self.tail == None):
           self.head = node
           self.tail = node
        else:
            node.next = self.head
            self.head = node

    def insert_tail(self, value): # O(1)
        node = self.Node(value)
        if (self.head == None) and (self.tail == None):
           self.head = node
           self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def delete_head(self): # O(1)
       if self.head == None:
           return print('Warning!! : No value, please insert the value')
       else:
           self.head = self.head.next

    def delete_tail(self): # O(n)
        if (self.head == None):
            return print('Warning!! : No value, please insert the value')
        elif (self.head == self.tail):
            self.head = None
        else:
            current = self.head
            while (current):
                if current.next.next:
                    current = current.next
                else:
                    current.next = None
                    self.tail = current
                    break






    # 여기서부턴 Singly_linked_list와 동일
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


list = SinglyLinkedListHasTail()
list.insert_head(5)
list.insert_head(3)
list.insert_head(1)

current = list.head
while current:
    print(current.value, end=' ')
    current = current.next


