###
# Calculates the sum of the digits in a number
#

def sum_digits(number):
    number = str(abs(number))
    fair = 0
    for char in range(1,len(number)+1):
       fair += int(number[char-1])
    return fair

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number is {result}')