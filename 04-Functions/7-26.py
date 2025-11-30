def f(text):
    dash_text = ''
    for char in text:
        dash_text = dash_text + '-' + char
    return dash_text[1:]

if __name__ == "__main__":
    print(f('UE'))