# 이름 : insertion sort(삽입 정렬)
# 방법 : 모든 값을 순회하며 자신의 위치를 찾는 방법
# Best : O(n^2)
# Worst : O(n)
# Space Complexity : O(1)
# Stability : Yes

def dahans_insertion_sort(x):
    if type(x) is list:
        for i in range(len(x)):
            while i > 0 and x[i-1] > x[i]:
                x[i-1], x[i] = x[i], x[i-1]
                i -= 1



a = [5, 4, 3, 2, 1]
dahans_insertion_sort(a)
print(a)