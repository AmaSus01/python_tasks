c = int(input())
a = 0
b = 0
for i in range(c):
    z = input()
    z = z.split(' ')
    if z[0] == 'север':
        b = b + int(z[1])
    elif z[0] == 'восток':
        a = a + int(z[1])
    elif z[0] == 'запад':
        a = a - int(z[1])
    elif z[0] == 'юг':
        b = b - int(z[1])
print(a, b)