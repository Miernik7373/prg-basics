def f(palindrome):
    half1 = ''
    half2 = ''
    half2_2 = ''
    g = len(palindrome)//2
    if len(palindrome)%2==0:
        half1 = palindrome[0:g]
        half2 = palindrome[g:]
        for char in half2:
            half2_2 = char + half2_2
        if half1 == half2_2:
            return True
        else:
            return False
    elif len(palindrome)%2==1:
        half1 = palindrome[0:g]
        half2 = palindrome[g+1:]
        for char in half2:
            half2_2 = char + half2_2
        if half1 == half2_2:
            return True
        else:
            return False
        
if __name__ == "__main__":
    print(f('kook'))