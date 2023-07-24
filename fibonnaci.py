n = int(input('enter the length of series-'))


def fibonacci():
    f1 = 0
    f2 = 1
    if n > 2:
        print("the fibonacci series of length", n, "-")
        for i in range(n):
            print(f2)
            f1 = f2
            f2 = f1 + f2
    elif n == 0:
        print(f1)
    elif n == 1:
        print(f2)
    else:
        print('enter positive inputs')


fibonacci()