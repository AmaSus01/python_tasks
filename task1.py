a = float(input())
b = float(input())
c = input()
result = 0.0
if c == 'mod':
    if b != 0:
        result = a % b
        print(result)
    else:
        print('Деление на 0!')
elif c == '*':
    result = a * b
    print(result)
elif c == '/':
    if b != 0:
        result = a / b
        print(result)
    else:
        print('Деление на 0!')
elif c == '+':
    result = a + b
    print(result)
elif c == '-':
    result = a - b
    print(result)
elif c == 'pow':
    if b != 0:
        result = a ** b
        print(result)
    else:
        print(1)
elif c == 'div':
    if b != 0:
        result = a // b
        print(result)
    else:
        print('Деление на 0!')












