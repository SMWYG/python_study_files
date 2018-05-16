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


    def push(self, value):
        self.list.append(value)
        current = len(self.list) - 1
        parent = self.__parent(current)
        while current > 0 and self.list[current] > self.list[parent]:
            self.list[current], self.list[parent] = self.list[parent], self.list[current]
            current = parent
            parent = self.__parent(current)
        return

    # def pop(self):
    #     if len(self.list) == 0:
    #         print('없음')
    #     else:
    #         return self.list[0]
    #
    #     last = self.list.pop()
    #     self.list[0] = last
    #     c = 0
    #     l = self.__left(c)
    #     r = self.__right(c)
    #
    #     if self.list[l] > self.list[r] or len(self.list) >= r:
    #         bigger = l
    #     else:
    #         bigger = r
    #
    #     if self.list[c] < self.list[bigger]:
    #         self.list[c], self.list[bigger] = self.list[bigger], self.list[c]
    #         c = bigger
    #         l = self.__left(c)
    #         r = self.__right(c)
    #         if self.list[l] > self.list[r] or len(self.list) >= r:
    #             bigger = l
    #         else:
    #             bigger = r
    #
    #     return

heap = MaxHeap()
for i in range(10):
    heap.push(i)
    print(i)

print(heap.list)
