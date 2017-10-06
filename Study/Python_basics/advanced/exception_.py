# exception vs error vs bug
# ■exception : 예외상황을 말한다. 그래서 예측이 가능하기 때문에 예외처리를 해준다.
# ■error : 잘못된 결과를 도출한 때를 말한다. 예측이 불가능하다.
# ■bug : 프로그래머에 의한 에러이다. 즉, 그냥 코드를 잘못 쓴 것


# 사용 방법
try:                                # 예외처리를 해야될 코드를 try문 안에서 실행한다.
    4/0
except ZeroDivisionError as e:      # 오류 메시지를 e에 담아준다.
    print(e)
else:                               # 오류가 나지 않았을 때 처리하는 문
    print("오류가 나지 않았습니다.")
    #pass                           # pass를 사용해 그냥 오류 메세지 띄우지 않고 넘길수도 있다.
finally:                            # 오류가 발생하던 하지 않던 무조건 실행되는 문 (보통 리소스를 close하는 것을 여기서 사용한다.)
    f.close()



