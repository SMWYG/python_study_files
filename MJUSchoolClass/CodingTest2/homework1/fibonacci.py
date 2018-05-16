def fibonacci(n):
    """
    피보나치 수열을 계산하는 함수를 작성하시오. 피보나치 수의 정의는 아래와 같다.

    f(n) = 0 if n = 0
    f(n) = 1 if n = 1
    f(n) = f(n-1) + f(n-2) if n > 1

    단 n에는 0 이상의 정수가 입력되는 것으로 가정하라.
    """

    n0 = 0
    n1 = 1
    tmp = 0
    result = 0

    if n == 0:
        return n0
    elif n == 1:
        return n1

    result = 1

    for _ in range(2,n):
        tmp = result
        result = result + tmp

    return result



    # if n == 0:
    #     return 0
    # elif n == 1:
    #     return 1
    # return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(11):
    print("f(%d) = %d" % (i, fibonacci(i)))

""" 수행 예: 
f(0) = 0
f(1) = 1
f(2) = 1
f(3) = 2
f(4) = 3
f(5) = 5
f(6) = 8
f(7) = 13
f(8) = 21
f(9) = 34
f(10) = 55
"""
