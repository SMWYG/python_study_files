# 이름 : heap sort(힙 정렬)
# 방법 : 힙 자료구조를 이용해 정렬하는 방법 (힙을 생성하는데 시간이 들어가는 것이 조금 아깝다.)
# Best : O(nlogn) best이더라도 결국엔 힙을 생성하는데 들어가는 nlogn이라는 시간은 있기 때문이다. 그리고 힙을 생성하는 과정 중 이 best가 의미가 거의 없어질 듯
# Worst : O(nlogn)
# Space Complexity : O(1) list로 구현한 heap이므로
# Stability : No

from Heap.my_heap import MaxHeap

def dahans_heap_sort(x):
    heap = MaxHeap()

    for i in x: # O(nlogn)
        heap.push(i)

    for i in range(len(x)):
        max_index = len(heap.list) - (i + 1)
        heap.list[0], heap.list[max_index] = heap.list[max_index], heap.list[0]
        heap.list[:len(heap.list) - (i + 1)] = heap.heapify(heap.list[:len(heap.list) - (i + 1)])

    return heap.list


a = [5, 4, 3, 2, 1]
a = dahans_heap_sort(a)
print('result!!! : ',a)