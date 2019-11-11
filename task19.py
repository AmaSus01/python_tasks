
def f(x):
    x = x*2
    return x


if __name__ == '__main__':
    n = int(input())
    d = {}
    for i in range(n):
        x = int(input())
        if x in d.keys():
           print(d[x])
        else:
            d[x] = f(x)
            print(d[x])
        '''
        if x not in d:
            k = (f(x))
            print(k)
            d[x] = [k]
            print(d)
        else:
            print(*d[x])
        '''


