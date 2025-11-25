PIN = ''
tries = 1
while tries<=3:
    PIN = input('Enter PIN code: ')
    if PIN == '0805':
        print('PIN correct.')
        break
    else: 
        print('Incorrect...')
        tries += 1
if tries == 4:
    print('Sorry, your payment card has been blocked.')