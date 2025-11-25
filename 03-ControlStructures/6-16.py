washing_product = input('Choose what will be washed (Jacket, underwear, shoes): ')
rinse = input('Is additional rinse programmed? (Yes/No): ')
if rinse == "Yes":
    rinse = True
else: rinse = False
spin = input('Is additional spin programmed? (Yes/No): ')
if spin == "Yes":
    spin = True
else: spin = False
time = 0
if washing_product == "jacket":
    time += 40
elif washing_product == "underwear":
    time += 70
elif washing_product == "shoes":
    time += 20
if rinse == True:
    time += 15
if spin == True:
    time += 9
print(f'Total washing time is: {time} minutes.')
