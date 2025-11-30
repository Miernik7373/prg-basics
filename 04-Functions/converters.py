def m_to_cm(n):
    return n*100

def cm_to_m(n):
    return n/100
def cm_to_inches(n):
    return n*2,54
def feetinches_to_cm(n: str):
    inches = 0
    for char in n:
        if char == "'":
            break
        inches += 12*int(char)

    g = len(n)-2
    z = len(n)
    for char in n[g:z]:
        if char == '"':
            break
        elif char == "'":
            continue
        inches += int(char)
    cm = 2*inches+(54/100)*inches
    return cm
    

if __name__ == "__main__":
    # only execute when you run this module
    # so you can test the functions in this place
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')
    a='"'
    print(f'{feetinches_to_cm("6'2")}')
