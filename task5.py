a = int(input())
b = int(input())
s = 0
k = 0
mid = float()
for i in range(a,b+1):
    if i % 3 == 0:
        k = k + 1
        s = s + i
mid = (s / k)
print(mid)
