#집합 자료형이란 집합에 관련된 것들을 쉽게 처리하기 위해 만들어진 자료형이다.
#중복을 허용하지 않는다.
#순서가 없다. (인덱싱 지원 안한다. 인덱싱으로 접근하려면 리스트나 튜플로 변환해야 한다.)
#set은 교집합, 합집합, 차집합을 구할 때 굉장히 유용하게 사용된다.
#집합 자료형으로는(함수) int랑 string만 사용될 수 있나봄

# 교집합
a=set([1,2,3,7,8,9])
b=set([1,2,3,4,5,6])
print(a&b)
print(a.intersection(b)) #교집합 함수

# 합집합
a=set([1,2,3,7,8,9])
b=set([1,2,3,4,5,6])
print(a|b)
print(a.union(b)) #합집함 함수

# 차집합
a=set([1,2,3,7,8,9])
b=set([1,2,3,4,5,6])
print(a-b)
print(a.difference(b))

#값 1개 추가 => add()
a.add(10)
print(a)

#값 여러 개 추가 => update()
a.update([11,12])
print(a)

#특정 값 제거 => remove()
a.remove(2)
print(a)
    #하나의 값 씩만 제거가 가능한듯

