with open('/home/amasus/Downloads/dataset_3363_3.txt', 'r') as inf:
    d = {}
    for line in inf:
        line = line.strip().upper().split()
        k = 1
        for i in line:
            if i in d.keys():
                d[i] += 1
            else:
                d[i] = k
    print(d)

    '''

    '''
