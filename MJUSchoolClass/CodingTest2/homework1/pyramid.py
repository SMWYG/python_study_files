def pyramid(height):
    """ 높이가 height인 삼각형을 아래와 같이 출력하는 함수를 작성하시오.
    단 height는 1 이상인 양수가 입력되는 것으로 가정하시오.
    print("<string>", end="") 와 같이 출력하면 줄바꿈 없이 문자열을 출력할 수 있다.
    """
    for i in range(height):
        print(' '*(height-i)+'*'*(i+(i+1)))

pyramid(1)
print("")
pyramid(3)
print("")
pyramid(5)
print("")

"""
수행 예:
*

  *
 ***
*****

    *
   ***
  *****
 *******
*********
"""
