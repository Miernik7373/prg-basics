###
# Checks if the given day number of the month is correct
#
month = int(input('Enter month number (1..12): '))
day = int(input('Enter the day number of the month: '))
day_ok = False

if month<8 and month%2 == 1:
    if day >=1 and day <= 31:
        day_ok = True
elif month>=8 and month%2 == 0:
    if day >=1 and day <= 31:
        day_ok = True
elif month<8 and month%2 == 0 and month != 2:
    if day >=1 and day <= 30:
        day_ok = True
elif month>=8 and month%2 == 1:
    if day >=1 and day <= 30:
        day_ok = True
if month == 2:
    if day>=1 and day<=28:
        day_ok = True
message = f'Day {day} for the month {month}'
if day_ok:
    print(f'{message} is correct')
else:
    print(f'{message} is incorrect')