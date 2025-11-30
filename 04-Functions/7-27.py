def f(product_code):
    true_code = product_code[:-1]
    g = len(product_code)
    divider = int(product_code[g-1])
    dividable = 0
    for char in true_code:
        dividable += int(char)
    if dividable%7 == divider:
        return True
    return False

if __name__ == "__main__":
    print(f('7071'))