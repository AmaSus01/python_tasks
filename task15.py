def f(x):
    if x <= -2:
        return 1-(x**2 + 2*x*2 + 4)
    elif -2 < x <= 2:
        return -(x/2)
    elif 2 < x:
        return (x**2 - 2*2*x + 4) + 1


if __name__ == '__main__':
    x = float(input())
    print(f(x))
