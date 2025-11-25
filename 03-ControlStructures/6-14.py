facebook = True
instagram = True
twitter = False

if twitter and instagram and facebook == True:
    print('You are a good influencer!')
elif twitter and instagram == True:
    print('You are a good influencer!')
elif twitter and facebook == True:
    print('You are a good influencer!')
elif facebook and instagram == True:
    print('You are a good influencer!')
else:
    print('You are a bad influencer!')