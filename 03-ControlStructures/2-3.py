
number1 = input("Wpisz pierwszą liczbę: ")
number1 = int(number1)
number2 = input("Wpisz drugą liczbę: ")
number2 = int(number2)
operator = input("Wpisz rodzaj działania (+/-/*/:): ")

if operator == "+":
    result = number1+number2
elif operator == "-":
    result = number1-number2
elif operator == "*":
    result = number1*number2
elif operator == ":":
    result = number1/number2
# print result
print(f'{number1} {operator} {number2} = {result}')
