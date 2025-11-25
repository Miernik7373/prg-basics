price = int(input('Enter the price: '))
amount = int(input('Enter amount: '))
price_down = 0
total_price = 0
if amount>=3:
    price_down = 3*price/4
    total_price = 2*price+(amount-2)*price_down
elif amount<3:
    total_price = amount*price
print(f'Number of products purchased: {amount}')
print(f'Product price: {price}')
print(F'Amount to pay: {total_price}')

