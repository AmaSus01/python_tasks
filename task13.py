str = input()
split_str = str.split(' ')
x = input()
k = 0
for i in range(len(split_str)):
    if split_str[i] == x:
        print(i, end=' ')
        k += 1
if k == 0:
    print('Отсутствует')