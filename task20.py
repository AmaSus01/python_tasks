
with open('exm.txt', 'r') as inf:
    s = inf.readline()
    i = 0
    for i in range(len(s)):
        k = 1
        if s[i].isdigit() and s[i-1].isdigit():
            pass
        elif s[i].isdigit() and s[i+1].isdigit():
            c = s[i] + s[i+1]
            while k != int(c):
                k += 1
                print(s[i-1], sep='', end='')
        elif s[i].isdigit():
            while k != int(s[i]):
                k += 1
                print(s[i-1], sep='', end='')
        else:
            print(s[i], sep='', end='')

        #  if s[i].isdigit() and s[i+1].isdigit():
        #     values_sum = s[i]+s[i+1]
        #    while k != int(values_sum):
        #       print(s[i-1], sep='', end='')
        #      k += 1
        # i += 2
        # else:
        #   print(s[i], sep='', end='')
        #  i += 1
