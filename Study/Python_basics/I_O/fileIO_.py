#■■■ 파일 생성 ■■■#
# 파일 생성하기
a=open("dahanchoi.txt","w")
a.close()
    # open()함수로 파일을 생성할 수 있다. 그러면 a에는 파일의 객체가 들어가게 된다.
    # r : 읽기 모드
    # w : 쓰기 모드 (생성되어 있는 파일을 이 모드로 또 실행시키면 있던 내용이 모두 사라짐)
    # a : 추가 모드 (파일의 내용을 추가하거나 변경하고 싶을 때)


# 파일에 내용 쓰기
a=open("dahanchoi.txt","a")
line1="안녕하세요\n"
line2="최다한입니다."
a.write(line1)
a.write(line2)
a.close()




#■■■ 파일 받아오기 ■■■#
# 외부에 저장된 파일을 읽어오는 방법에는 세가지가 있다.

# 1. readline() 이용
a=open("dahanchoi.txt", "r")
while True:
    line = a.readline()
    if not line :
        break
    print(line)
a.close()
    # readline()는 파일의 내용을 한 줄씩 읽어오는 함수(문자열로 읽어들임)로 더 이상 읽을 라인이 없을 경우에는 None을 반환한다.


# 2. readlines() 이용
a=open("dahanchoi.txt", "r")
lines = a.readlines()
for i in lines:
    print(i)
a.close()
    # readlines()는 readline()과 달리 모든 라인을 한번에 읽어오는 함수이다. (각 라인을 문자열로 가져와 하나의 리스트에 담는다.)


# 3. read() 이용
a=open("dahanchoi.txt", "r")
alld = a.read()
print(alld)
for i in range(len(alld)):
    print(alld[i])
    # read()는 파일의 내용 전체를 문자열로 묶어 리턴한다.


# with문 사용해서 파일 입출력하기
# with문을 이용하면 with 블록을 벗어나는 순간 객체가 close 되기 때문에 편하다.
with open("dahanchoi.txt", "r") as a:
    alld = a.read()
    print(alld)