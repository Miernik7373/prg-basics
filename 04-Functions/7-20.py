
def f(n):
    if n < 1:
        return "n musi być >= 1"
    
    count = 0     
    num = 2       
    
    while True:

        is_prime = True
        i = 2

        while i * i <= num:
            if num % i == 0:
                is_prime = False
                break
            i += 1
        
        if is_prime:
            count += 1
            if count == n:
                return num
        num += 1

if __name__ == "__main__":
    print(f(2))