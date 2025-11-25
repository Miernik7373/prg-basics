
###
# Calculates the sum of even numbers from 1 to a given number N
#
N = 12
sum_even = 0
number = 1
# Calculate the sum of even numbers
while 0<number<N:
    number += 1
    if number % 2 == 0:
        sum_even += number
    if number == N:
        break

print(f"The sum of even numbers from 1 to {N} is: {sum_even}")