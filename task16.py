def modify_list(l):
    l[:] = [i // 2 for i in l if not i % 2]


if __name__ == '__main__':
    lst = [i for i in range(1, 10)]
    print(lst)
    modify_list(lst)
    print(lst)
