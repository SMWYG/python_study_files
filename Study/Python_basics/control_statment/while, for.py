#■■■ while 기본 형태  ■■■#
while 1:
    print("한번은 출력될거야!")
    if 1:
        break                            #강제로 while문 빠져나오게 하기 위한 명령어
    if 2:
        continue                         #while문의 시작점으로 돌아가게 하기 위한 명령어





#■■■ for 기본 형태  ■■■#
a=[1,2,3]                                #for문에는 리스트, 튜플, 문자열이 들어갈 수 있음.
for i in a:
    print(i)

#튜플을 사용한 for문
a=[(2,2),(3,3)]
for (i,j) in a:
    print(i+j)


#리스트를 사용한 for문
a=[[1,2,3],[3,4,5]]
for (i,j,k) in a:
    print(i+j+k)


#zip()함수를 사용한 for문
a=[1,2,3,4,5]                           #zip()은 각 리스트의 인덱스별로 묶어서 하나의 리스트로 만들어준다.
b=[5,4,3,2,1]
for (i,j) in zip(a,b):
    print(i+j)


#range()을 사용한 for문
for i in range(10):
    print(i)


#range() 범위 정의
for i in range(0,10):
    print(i)







#■■■ 리스트안에 for문  ■■■#
result=[num*3 for num in range(5)]                                          #for문 뒷 순으로 연산 시작이며 for문 앞에 있는것이 최종연산임
print(result)

#if 조건 주기
result=[num*3 for num in range(5) if num%2==0]
print(result)

#중복 for문
result=[x*y for x in range(1,5) for y in range(1,5)]
print(result)