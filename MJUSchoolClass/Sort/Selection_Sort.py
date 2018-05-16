# 이름 : selection sort(선택 정렬)
# 방법 : 모든 값을 순회하며 최소(최대)값을 찾는 방법
# Best : O(n^2)
# Worst : O(n^2)
# Space Complexity : O(1)
# Stability : No [ ex) b1, b2, a, c  =>  a, b2, b1, c]

def dahans_selection_sort(x):
    if type(x) is list:
        for i in range(len(x)):
            min_value_index = i
            for j in range(i+1, len(x)):
                if x[j] < x[min_value_index]:
                    min_value_index = j
            x[i], x[min_value_index] = x[min_value_index], x[i]

a = [5,4,3,2,1]
dahans_selection_sort(a)
print(a)