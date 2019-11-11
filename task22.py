with open('exm.txt', 'r') as inf:
    g = 0
    first_mark = 0
    second_mark = 0
    third_mark = 0
    for line in inf:
        g += 1
        z = 0
        k = 0
        mid = 0
        chek = 1
        line = line.strip().split(';')
        for i in range(len(line)):
            if line[i].isdigit():
                if chek == 1:
                    chek += 1
                    first_mark += int(line[i])
                elif chek == 2:
                    chek += 1
                    second_mark += int(line[i])
                elif chek == 3:
                    chek = 0
                    third_mark += int(line[i])
                z += float(line[i])
                k += 1
        if z > 0 and k > 0:
            print(z / k)
    print(first_mark / g, second_mark / g, third_mark / g)
