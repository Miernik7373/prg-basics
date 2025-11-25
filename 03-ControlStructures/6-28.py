k = 0
g = 0
for i in range(1,20):
    if i == 2:
        g = 1
    z = k+g
    k = g
    g = z
    print(f'{z}', end = " ")

