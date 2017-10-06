#■■■ 기본 형태  ■■■#
if 1:
    print("참")
    pass                        #pass는 해당 조건에 해당되었을 때 아무일도 하지 않겠다라는 뜻이다.
elif 0:                         #elif를 통해 다양한 조건을 추가로 줄 수 있음
    print("거짓")
else:
    print("거짓")


#and, or, not 연산자
if 1 or 0:
    print("참")
else:
    print("거짓")


#in, not in 연산자
#이는 리스트[], 튜플(), 문자열""에 사용되는 연산자이다.
a="abcde"
print("a" in a)
print("a" not in a)





#■■■ 간단한 형태(한줄)  ■■■#
#if문안의 내용이 pass 거나 한줄로 끝이 난다면 이 형태를 쓰기를 추천
if 1:pass
else:print("거짓")