'''
Шифровка
'''
a = input()
b = input()
z = ''
for i in range(len(a)):
    if a[i].isalpha():
        z += a[i]
print(z)