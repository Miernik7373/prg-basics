ean = str(input('Enter EAN: '))
if len(ean) != 13:
    print("Invalid EAN.")
else:
    if ean[0:3] == "590":
        print('Article manufactured in Poland.')
    else: 
        print('Article not manufactured in Poland.')