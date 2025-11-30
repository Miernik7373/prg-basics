def f(binary_number):
    good = '01'
    status = True
    for char in binary_number:
        if char not in good:
            status = False
            break
        else:
            status = True
    return status
print(f('0110001000'))