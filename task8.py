str = input()
sum = 0
str_split = str.split(' ')
for i in range(len(str_split)):
    sum += int(str_split[i])
print(sum)


