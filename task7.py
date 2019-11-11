a = input()
i = 0
k = 1
while i < len(a)-1:
    if a[i] == a[i+1]:
        i += 1
        k += 1
    else:
        print(a[i], k, sep='', end='')
        i += 1
        k = 1
print(a[i], k, sep='', end='')