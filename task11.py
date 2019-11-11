n = int(input())
squr = 0
sum = 0
k =0
while n != 0:
    sum += n
    squr += (n*n)
    if sum == 0:
        print(squr)
        break
    n = int(input())

