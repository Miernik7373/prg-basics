hour = input('Enter time (24 hour format): ')
am_pm = 'am'
time = int(hour[0:2])
minutes = hour[3:5]

if int(hour[0:2])>12:
    time = str(time - 12)
    am_pm = 'pm'
    print(f'Time in 12-hour format: {time}:{minutes}{am_pm}')
elif hour == '00:00':
    print(f'Time in 12-hour format: 12:00am')
else:
    print(f'Time in 12-hour format: {time}:{minutes}{am_pm}')

