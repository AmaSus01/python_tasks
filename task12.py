n = int(input())
k = 0
for i in range(1, n):
    for j in range(i):
        k += 1
        print(i)
        if k == n:
           break