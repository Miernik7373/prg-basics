###
# House lighting with three bulbs and two switches
# Checking how many bulbs are illuminating the house
#
light_switch1 = False # False - switch off, True - switch on
light_switch2 = False
bulbs_on = 0
while True:
    switch_option1 = input('Switch the first switch? (Y/N): ')
    if switch_option1 == "Y":
        light_switch1 = True
    elif switch_option1 == "N":
        light_switch1 = False
    else:
        print('Ooops, you missed it!')
    if switch_option1 == "Y" or "N":
        break
while True:
    switch_option2 = input('Switch the second switch? (Y/N): ')
    if switch_option2 == "Y":
        light_switch2 = True
    elif switch_option2 == "N":
        light_switch2 = False
    else:
        print('Ooops, you missed it!')
    if switch_option2 == "Y" or "N":
        break
if light_switch1 == True:
    bulbs_on += 1
if light_switch2:
    bulbs_on +=2
if bulbs_on >= 2:
    print(f'There are {bulbs_on} lightbulbs lit.')
elif bulbs_on == 1:
    print('There is one lightbulb lit.')
else:
    print('There are no lighbulbs lit.')