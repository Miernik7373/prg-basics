def f(detector):
    count = 0
    for char in detector:
        if count != 3:
            if char == '+':
                count += 1
            elif char == '-':
                count -= 1
        elif count == 3:
            return True
    return False

if __name__ == '__main__':
    print(f('+-++-++-+---'))