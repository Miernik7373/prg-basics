n1 = int(input("Input speed (mps): "))
converter = lambda n1: n1*3.6
print(f'{n1}m/s = {int(converter(n1))} km/h')