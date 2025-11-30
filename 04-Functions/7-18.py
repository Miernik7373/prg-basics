def f(sentence):
    space = " "
    sentence_plus = ''
    for char in sentence:
        if char in space:
            char = ""
        sentence_plus = sentence_plus + char
    return sentence_plus



if __name__ == "__main__":
    print(f('A programming language is a system of notation for writing computer programs'))