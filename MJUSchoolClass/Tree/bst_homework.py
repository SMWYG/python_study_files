"""
아래에 학번과 이름을 꼭 적으세요.

학번: 60131271
이름: 최다한
"""
import random
import pandas as pd

class BinarySearchTree:
    class Node:
        def __init__(self, key, value, left, right):
            self.key = key
            self.value = [value]
            self.left = left
            self.right = right

    def __init__(self):
        self.root = None
        self.key_count = 0
        self.value_count = 0

    def insert(self, key, value):
        self.root = self.__insert(self.root, key, value)
        self.value_count += 1

    def __insert(self, node, key, value):
        # 여기에 Tree의 노드에 key, value를 insert하는 알고리즘을 작성하시오.
        # 새로운 키가 추가되면 key_count도 증가시켜야 함 (동일한 키가 들어오는 경우는 증가 안함)
        if self.root == None:
            new_node = self.Node(key, value, None, None)
            self.root = new_node
            self.key_count += 1
        elif node.key == key:
            node.value.append(value)
        elif node.key > key:
            if node.left:
                self.__insert(node.left, key, value)
            else:
                new_node = self.Node(key, value, None, None)
                node.left = new_node
                self.key_count += 1
        elif node.key < key:
            if node.right:
                self.__insert(node.right, key, value)
            else:
                new_node = self.Node(key, value, None, None)
                node.right = new_node
                self.key_count += 1
        return self.root

    def in_order(self):
        for x in self.__in_order(self.root):
            yield x

    def __in_order(self, node):
        if not node:
            return
        if node.left:
            for n in self.__in_order(node.left):
                yield n
        yield node
        if node.right:
            for n in self.__in_order(node.right):
                yield n

    def find(self, key):
        return self.__find(self.root, key)

    def __find(self, node, key):
        # 키가 존재하지 않으면 [] (빈 리스트)를 반환하시오.
        # 키가 존재하면 node.value를 반환하시오.
        if node == None:
            return []
        elif node.key == key:
            return node.value
        elif node.key > key:
            return self.__find(node.left, key)
        elif node.key < key:
            return self.__find(node.right, key)

    def height(self):
        return self.__height(self.root)

    def __height(self, node):
        # 주어진 노드의 높이를 반환하는 알고리즘을 작성하시오.
        if node == None:
            return 0
        left = 1 + self.__height(node.left)
        right = 1 + self.__height(node.right)

        return max(left, right)


def print_stat(tree):
    print(f"Height = {tree.height()}")
    print("{:,} keys / {:,} values".format(tree.key_count, tree.value_count))


if __name__ == "__main__":
    #-------------------------------------------------
    # # 간단한 BST 테스트
    # tree = BinarySearchTree()
    # tree.insert(5, "F")
    # tree.insert(3, "E")
    # tree.insert(8, "D")
    # tree.insert(9, "C")
    # tree.insert(10, "B")
    # tree.insert(11, "X")
    # tree.insert(1, "A")
    # for x in tree.in_order():
    #     print(f"{x.key}:{x.value}", end="->")
    # print()
    # print("Key=6", tree.find(6)) # 'C'
    # print("Key=4", tree.find(4)) # None
    # print("Key=1", tree.find(1)) # 'A'
    # print("Key=5", tree.find(5)) # 'F'
    # print("Key=9", tree.find(9)) # None
    # print_stat(tree)

    #-------------------------------------------------
    # 10만개 데이터 넣는 실험
    # t = BinarySearchTree()
    # for i in range(1000):
    #     k = random.randint(0, 1000)
    #     t.insert(k, f"DATA {i}")
    # print_stat(t)

    #-------------------------------------------------
    # 세익스피어의 희곡에서 단어를 검색하는 실험
    # 단어를 입력하면 해당 단어가 나오는 희곡의 라인을 검색해줌.

    bst = BinarySearchTree()

    # csv 파일을 읽어들인다.
    df = pd.read_csv('./Shakespeare_data.csv', dtype=str)
    print("Indexing all data ...")
    for index, row in df.iterrows():
        # 대사를 단어단위로 잘라 keys 리스트에 저장하고, 전체 행은 합쳐 value에 저장한다.
        keys = [x.upper() for x in row[5].split(" ")]
        value = " ".join([x for x in row if str(x) != 'nan'])
        for key in keys:
            # 각 key, value를 트리에 저장한다.
            bst.insert(key, value)
    print("Done")
    print_stat(bst)
    while True:
        # 사용자에게 keyword를 입력받아서 트리에서 찾아준다.
        keyword = input(">> Enter keyword ('\\q' for quit) : ")
        if keyword == '\\q':
            break
        result = bst.find(keyword.upper())
        print("\n".join(result))
        print("--- Found {} lines".format(len(result)))

