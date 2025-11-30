def f(n1,n2,n3):
    if n1>0 and n2>0 and n3<0:
        return True
    elif n1>0 and n2<0 and n3>0:
        return True
    elif n1<0 and n2>0 and n3>0:
        return True
    else:
        return False
    
if __name__ == '__main__':
    print(f(-1,2,3))