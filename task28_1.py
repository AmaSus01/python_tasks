



if __name__ == "__main__":
    d_sum = {'1': [0,0], '2': [0,0], '3': [0,0], '4': [0,0], '5': [0,0], '6': [0,0], '7': [0,0], '8': [0,0], '9': [0,0], '10': [0,0], '11': [0,0]}
    d_result = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0}

    with open('exm.txt', 'r') as inf:
        for line in inf:
            s = line.split()

            if s[0] == '1':
                d_sum['1'][0] += int(s[2])
                d_sum['1'][1] += 1
            elif s[0] == '2':
                d_sum['2'][0] += int(s[2])
                d_sum['2'][1] += 1
            elif s[0] == '3':
                d_sum['3'][0] += int(s[2])
                d_sum['3'][1] += 1
            elif s[0] == '4':
                d_sum['4'][0] += int(s[2])
                d_sum['4'][1] += 1
            elif s[0] == '4':
                d_sum['5'][0] += int(s[2])
                d_sum['5'][1] += 1
            elif s[0] == '6':
                d_sum['6'][0] += int(s[2])
                d_sum['6'][1] += 1
            elif s[0] == '7':
                d_sum['7'][0] += int(s[2])
                d_sum['7'][1] += 1
            elif s[0] == '8':
                d_sum['8'][0] += int(s[2])
                d_sum['8'][1] += 1
            elif s[0] == '9':
                d_sum['9'][0] += int(s[2])
                d_sum['9'][1] += 1
            elif s[0] == '10':
                d_sum['10'][0] += int(s[2])
                d_sum['10'][1] += 1
            elif s[0] == '11':
                d_sum['11'][0] += int(s[2])
                d_sum['11'][1] += 1

    for i in d_sum.keys():
        high = d_sum[i][0]
        amount = d_sum[i][1]
        try:
            res = high / amount
        except ZeroDivisionError:
            res = '-'
        d_result[i] = res

    print(d_result)