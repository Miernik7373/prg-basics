def f(number):
    true = 0
    number = str(number)
    g = len(number)
    for i in range(1,g):
        i = str(i)

        if number.count(i) >= 2:
            true += number.count(i)*int(i)
    return true

if __name__ == "__main__":
    print(f(113447772))