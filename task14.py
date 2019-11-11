n = int(input())
k = 0
for i in range(1, n*n+1):
    if k < n:
        print(i, end=' ')
        k += 1
    else:
        print('')
        print(i, end=' ')
        k = 1


