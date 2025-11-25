current_price = int(input('Enter current price: '))
previous_price = int(input("Enter previous price: "))
discount = current_price/previous_price*100
if discount<=90:
    print('Buy the product!')
else: 
    print("Don't buy the product!")
print(f'Product price reduced by: {100-discount}%')