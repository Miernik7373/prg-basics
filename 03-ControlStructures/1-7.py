###
# Program that calculates the employee's salary,
# taking into account the possibility of receiving a bonus.
#
basic_salary = 5000
bonus = 0.30 
total_salary = basic_salary*bonus+basic_salary
is_bonus = input('Does the employee receive a bonus? (Y/N):') == 'Yes'

if is_bonus:
    total_salary = basic_salary*bonus+basic_salary

else:
    total_salary = basic_salary

print(f'Basic salary: {basic_salary}')
print(f'Bonus included? {is_bonus}')
print(f'Total salary: {total_salary}')