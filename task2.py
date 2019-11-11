a = int(input())
b = int(input())
d = 1
while d > 0:
    if d % a == 0 and d % b == 0:
        print(d)
        break
    else:
        d = d + 1


