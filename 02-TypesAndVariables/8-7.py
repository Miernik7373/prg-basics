decimal =int(input("Write decimal number: "))
print(f'binary: {int((decimal/2**7))%2}b{int((decimal/2**6))%2}{int((decimal%2**5))%2}{int((decimal/2**4))%2}{int((decimal/2**3))%2}{int((decimal/2**2))%2}{int((decimal/2)%2)}{decimal%2}')


hex_chars = "123456789ABCDEF"
first = decimal //16**2
second = decimal // 16
third = decimal%16
thrid = int(third)
print(f'heksadecimal: {hex_chars[first]}x{hex_chars[second]}{hex_chars[third]}') 

