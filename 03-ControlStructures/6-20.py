decimal1 = int(input('Enter decimal number: '))
decimal = decimal1
end = 0
binary = ''
number = 0
while end<decimal:
    number = decimal%2
    decimal = decimal//2
    binary = str(number) + binary
print(f'{decimal1}(10) = {binary}(2)')