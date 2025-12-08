sentence = 'I completely agree with you'
arr = sentence.split()
result = list(map(lambda x: len(x), arr))
print(result)