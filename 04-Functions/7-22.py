def f(name):
    name = " " + name
    count = ""
    add = 0
    number = len(name)
    for char in name:
        add += 1
        if char == " ":
            count += name[add]
    return count

if __name__ == "__main__":
    print(f("Python"))
    