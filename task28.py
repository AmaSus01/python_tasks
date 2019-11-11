with open('exm.txt', 'r') as inf:
    d = {}
    k = 1
    for line in inf:
        s = line.strip().split()
        # s = re.sub('\s+',' ', s)
        if s[0] not in d.keys():
            d[s[0]] = int(s[2])
        else:
            d[s[0]] += int(s[2])
print(d)
