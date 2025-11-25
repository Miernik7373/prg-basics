
N = int(input("Podaj ile liczb pierwszych chcesz wyświetlić: "))
count = 0
num = 2

while count < N:
    for j in range(2, num):
        if num % j == 0:
            break
    else:
        print(num, end=' ')
        count += 1
    num += 1
