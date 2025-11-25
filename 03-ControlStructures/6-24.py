
# Program do wyświetlenia wzoru gwiazdek

# Liczba maksymalnych gwiazdek w środkowym wierszu
n = 5

# Część rosnąca
for i in range(1, n + 1):
    print("* " * i)

# Część malejąca
for i in range(n - 1, 0, -1):
    print("* " * i)


for char in range(10,0,-1):
    print(char)