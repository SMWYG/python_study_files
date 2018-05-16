'''
■ 전체적인 구조
만들 자료구조 : Heap (Max Heap)
Heap의 특징 : Complete Binary Tree, 맥스힙이므로 부모는 항상 자식보다 크다.
구현 방법 : array
구현해야 할 기능 : push, pop
Big O notation : push(logN), pop(pogN)
'''

class MaxHeap:
    def __init__(self):
        self.list = []

    def __parent(self, i):
        return int((i + 1) / 2) - 1

    def __left(self, i):
        return 2 * i + 1

    def __right(self, i):
        return 2 * i + 2

    def __getBigger(self, l, r, list):
        if r > len(list) - 1: # r이 없으면
           if l > len(list) - 1: # l도 없으면
               return None
           else:
               return l
        else:
            return l if list[l] > list[r] else r

    def heapify(self, sub_list):
        if len(sub_list) in (0, 1):
            return sub_list
        else:
            current = 0
            l_child = self.__left(current)
            r_child = self.__right(current)
            bigger_child = self.__getBigger(l_child, r_child, sub_list)

            while bigger_child:
                sub_list[current], sub_list[bigger_child] = sub_list[bigger_child], sub_list[current]
                current = bigger_child
                l_child = self.__left(current)
                r_child = self.__right(current)
                bigger_child = self.__getBigger(l_child, r_child, sub_list)

            return sub_list

    def push(self, value):
        # edge case1 : 비워져 있는 경우 -> 리스트가 비어서 맨뒤에 넣어 그 패런츠를 참조할 때 에러가 날 수 있음
        # edge case2 : 하나만 채워져 있는 경우
        if len(self.list) == 0: # edge1 해결
            self.list.append(value)
        elif len(self.list) == 1: # edge2 해결
            self.list.append(value)
            current = len(self.list)-1
            parent = self.__parent(current)

            if self.list[current] > self.list[parent]:
                self.list[current], self.list[parent] = self.list[parent], self.list[current] # 파이썬에서 제공하는 자동 스왑기능 tmp 필요 x
        else: # 일반적인 경우
            self.list.append(value)
            current = len(self.list)-1
            parent = self.__parent(current)

            while current > 0 and self.list[current] > self.list[parent]:
                self.list[current], self.list[parent] = self.list[parent], self.list[current]
                current = parent
                parent = self.__parent(current)

    def pop(self):
        if len(self.list) == 0:
            return
        elif len(self.list) == 1:
            return self.list.pop()
        else:
            result = self.list[0] # 마지막에 result return 할 것임 일단 keep
            self.list[0] = self.list.pop()

            current = 0
            l_child = self.__left(current)
            r_child = self.__right(current)
            bigger_child = self.__getBigger(l_child, r_child, self.list)

            while bigger_child:
                if self.list[current] > self.list[bigger_child]:
                    return result
                else:
                    self.list[current], self.list[bigger_child] = self.list[bigger_child], self.list[current]
                    current = bigger_child
                    l_child = self.__left(current)
                    r_child = self.__right(current)
                    bigger_child = self.__getBigger(l_child, r_child, self.list)

            return result






if __name__ == "__main__":
    heap = MaxHeap()


    for i in range(15):
        heap.push(i)

    print(heap.list)
    result = []

    for i in range(15):
        print(heap.pop())
        # result.append(heap.pop())

    # print(result)

