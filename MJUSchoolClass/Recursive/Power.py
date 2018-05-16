import timeit

def power_i(x,n): # O(n)
    sum = 1
    for _ in range(n):
        sum = sum*x
    return sum

def power_r(x,n): # O(n)
    if n == 0:
        return 1
    return x*power_r(x,n-1)

def power_r2(x,n): # O(n)
    if n == 0:
        return 1
    elif n%2 == 0:
        return (power_r2(x,n//2))**2
    else:
        return x*power_r2(x,n-1)

print(power_r2(2,12))
# for i in range(1000):
#     if i%100 == 0 :
#         start_time1 = timeit.default_timer()
#         power_r(2,i)
#         end_time1 = timeit.default_timer()
#         elapsed1 = end_time1 - start_time1
#         start_time2 = timeit.default_timer()
#         power_i(2,i)
#         end_time2 = timeit.default_timer()
#         elapsed2 = end_time2 - start_time2
#         start_time1 = timeit.default_timer()
#         power_r2(2,i)
#         end_time1 = timeit.default_timer()
#         elapsed3 = end_time1 - start_time1
#         print("Count(%d)     R:%0.8fseconds  I:%0.8fseconds  R2:%0.8fseconds" %(i,elapsed1,elapsed2,elapsed3))