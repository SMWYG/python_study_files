def hanoi(n,base,target,tmp):
    if n == 0:
        return
    hanoi(n-1, base, tmp, target) # n이 1일 때 return 되므로 무조건 1임 n은
    print("Disk %d: %s --> %s"%(n, base, target))
    hanoi(n-1, tmp, target, base)

hanoi(3,"a","b","c")