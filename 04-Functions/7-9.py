def f(number,even):
    dict = "02468"
    result = 0
    number = str(number)
    for i in number:
        if even == True:
            if i in dict:
                i = int(i)
                result += i
        else:
            if i not in dict:
                i = int(i)
                result += i
    return result
print(f(13115,True))