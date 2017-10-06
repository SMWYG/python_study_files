#딕셔너리란 대응관계를 나타내는 자료형으로 다른 곳에선 연관 배열 및 해시라고도 불리운다.
#value와 key를 사용하는 자료형이다. 그래서 리스트나 튜플처럼 순차적(sequential)으로 요소값을 찾지 않고 key를 통해 해당 value를 찾게 된다.

#■■■ 쌍 추가, 삭제 ■■■#

#쌍 추가
a={1:"apple"}
a[2]="banana"
print(a)
    #key값은 고유해야 함
    #key로 리스트는 올 수 없음 (변환의 가능성이 있으므로) 튜플은 사용 가능

#쌍 삭제
del a[2]
print(a)





#■■■ 딕셔너리 관련 함수 ■■■#

#key 목록(리스트) 만들기 => keys()
a={1:"apple", 2:"banana"}
print(a.keys())
    #2.7버전까지는 list 형태로 만들어지지만 3버전 이후에는 dict_keys라는 형태로 만들어짐

#key, value쌍 목록(튜플) 만들기 => items()
print(a.items())


#key, value쌍 모두(딕셔너리 내용 모두) 삭제 => clear()
print(a.clear())

#key로 value값 가져오기 => get()
a={1:"apple", 2:"banana"}
print(a.get(1))
    #a[1]로도 value를 가져올 수 있지만 해당 key가 딕셔너리에 없는 경우 설명없이 에러가 뜨지만 get을 사용할 경우 none을 띄우므로 get을 사용하는게 좋음.

#key로 value값 가져오기(값이 없을 경우 default 주기) => get()
a={1:"apple", 2:"banana"}
print(a.get(3,"sorry"))

#key가 딕셔너리에 있는지 확인하기 => in
a={1:"apple", 2:"banana"}
print(1 in a)