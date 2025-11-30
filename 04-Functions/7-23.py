def f(password):
    if len(password)<6:
        return False
    for char in password:
        if password.count(char) >= 2:
            return False
    return True

if __name__ == "__main__":
    print(f(''))