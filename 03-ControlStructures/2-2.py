driving_mode = input('Enter driving mode (A/M/E):')
distance = int(input('Enter distance in km: '))

if driving_mode == 'A':
    fuel_consumption = 7/100 # liters per 100km
elif driving_mode == 'M':
    fuel_consumption = 9/100    
elif driving_mode == 'E':
    fuel_consumption = 6/100    
total_consumption = fuel_consumption*distance
total_consumption=int(total_consumption)
print(f'Total fuel consumption over a distance of {distance} km in driving mode {driving_mode} is {total_consumption} liters')