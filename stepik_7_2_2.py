m = int(input())
n = int(input())
if m < n:
    for i in range(m,n + 1):
        print(i)
elif m == n: print(m)
else:
    for i in range(m,n - 1,-1):
        print(i)