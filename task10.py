str = input()
n = 1
split_str = str.split(' ')
split_str.sort()
for i in range(len(split_str)-1):
    if split_str[i] == split_str[-1]:
        print(split_str[i])
        break
    if split_str[i] == split_str[i+1] and split_str[i] != split_str[i-1]:
        print(split_str[i], end=' ')
















