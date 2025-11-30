def power(x,n):
    if x==0 or n==1 or x==1:
        return x
    if x>1:
        x = x*power(x,n-1)
    return x

if __name__ == "__main__":
    print(power(2,4))
