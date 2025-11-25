hours = int(input('Write the amount of hours you have used the parking: '))
price = 0
if 1<=hours<=2:
    price = 5
elif 3<=hours<=6:
    price = 15
elif 6<hours:
    price = 20
print(f'Your payment for the parking is {price} PLN.')