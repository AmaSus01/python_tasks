str = input()
split_str = str.split(' ')
l = len(split_str)
sum = 0
if len(split_str) == 1:
    print(str)
else:
    for i in range(len(split_str)):
        if i == 0:
            sum = int(split_str[-1]) + int(split_str[i+1])
            print(sum, end=' ')
        elif i == len(split_str) - 1:
            sum = int(split_str[0]) + int(split_str[i-1])
            print(sum, end=' ')
        else:
            sum = int(split_str[i+1]) + int(split_str[i-1])
            print(sum, end=' ')





    
