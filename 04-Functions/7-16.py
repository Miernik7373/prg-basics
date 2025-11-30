def f(n):
    if n == 1:
        fibo = 0
        return fibo
    elif n == 2:
        fibo = 1
        return fibo
    count = 2
    num1 = 0
    num2 = 1
    fibo = 0
    while count!=n:
        fibo = num1 + num2
        num1 = num2
        num2 = fibo
        count += 1
    return fibo
if __name__ == '__main__':
    print(f(5))