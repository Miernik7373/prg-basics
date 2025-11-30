
def input_string(message):
    entered = input(message)
    return entered

def input_integer(message):
    inputted = int(input(message))
    return inputted

def input_real(message):
    real = float(input(message))
    return real

def input_boolean(message):
    boolean = input(message)
    if boolean == 'y':
        boolean = False
    else:
        boolean = True
    return boolean

