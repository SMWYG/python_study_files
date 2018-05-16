import timeit

def factorial_r(n): # O(n)
    if n == 0:
        return 1 # 값이 안 죽기 위해서 0으로 두면 무조건 0으로 수렴
    else:
        return n*factorial_r(n-1)

def factorial_i(n): # O(n)
    f = 1
    for i in range(1,n+1):
        f *= i
    return f


for i in range(500):
    if i%10 == 0 :
        start_time1 = timeit.default_timer()
        factorial_r(i)
        end_time1 = timeit.default_timer()
        elapsed1 = end_time1 - start_time1
        start_time2 = timeit.default_timer()
        factorial_i(i)
        end_time2 = timeit.default_timer()
        elapsed2 = end_time2 - start_time2
        print("Count(%d)     R:%0.8fseconds  I:%0.8fseconds" %(i,elapsed1,elapsed2))