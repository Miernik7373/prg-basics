distance = int(input('Distance in km: '))
fuel_price = float(input('Fuel price for liter: '))
fuel_consumption = float(input('Fuel consumption in liters per 100km: '))
total_fuel_consumption = distance/100*fuel_consumption
total_cost = fuel_price*total_fuel_consumption
print(f'The total cost of transporting goods is: {total_cost}')