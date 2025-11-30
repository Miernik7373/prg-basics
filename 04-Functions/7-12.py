def f(n):
    asterisk = ""
    for char in range(0,n):
        char = '*'
        asterisk = asterisk + char + '/'
    asterisk = asterisk[0:len(asterisk)-1]
    return asterisk

if __name__ == "__main__":
    print(f(5))