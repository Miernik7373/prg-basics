value = int(input("Enter the amount in PLN: "))
five_pln = int(value/5)
two_pln = int(value%5/2)
if five_pln*5+two_pln*2 == value:
    one_pln = 0
else:
    one_pln = 1
print(f' The amount of PLN {value} in coins: ')
print(f'5 PLN coins: {five_pln}')
print(f'2 PLN coins: {two_pln}')
print(f'1 PLN coins: {one_pln}')