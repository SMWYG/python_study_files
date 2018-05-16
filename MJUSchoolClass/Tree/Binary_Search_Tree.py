'''
■ 전체적인 구조
만들 자료구조 : Binary Search Tree
BST의 특징 : 왼쪽 자식은 부모보다 작고 오른쪽 자식은 부모보다 크다. 그 후손도 계속 작고 커야함
구현 방법 : Linked List (BST의 조건이 CBT는 아니므로 array로 구현 힘듬)
구현해야 할 기능 : insert, find, height
Big O notation :(balanced일 경우) insert(logN), find(logN), height(N)
'''

import random

class BST:
    class Node:
        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def add(self, key):
        self.root  = self.__add_node(self.root, key)

    def __add_node(self, node, key):
        if node:
            if node.key > key:
                node.left = self.__add_node(node.left, key)
            elif node.key < key:
                node.right = self.__add_node(node.right, key)
        else:
            node = self.Node(key)
        return node

    def inorder(self):
        self.__inorder(self.root)
        print()

    def __inorder(self, node):
        if node:
            self.__inorder(node.left)
            print(node.key, end=' ')
            self.__inorder(node.right)

    def height(self):
        return self.__height(self.root)

    def __height(self, node):
        if not node:
            return 0
        l = self.__height(node.left)
        r = self.__height(node.right)
        return max(l,r) + 1

    def search(self, value):
        return self.__search(self.root, value)

    def __search(self, node, value):
        if not node:
            return False
        elif node.key == value:
            return True
        elif node.key > value:
            return self.__search(node.left, value)
        else:
            return self.__search(node.right, value)



t = BST()

for _ in range(10):
    t.add(random.randint(0,10))

print(t.inorder())
print(t.search(3))



