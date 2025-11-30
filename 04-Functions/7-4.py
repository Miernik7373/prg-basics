def count(sentence):
    vowel = 'e'
    number = 0
    for char in sentence:
        if char == vowel:
            number += 1
    return number
print(count('You never get a second chance to make a first impression'))