import random
dice_roll = random.randint(0,6)
dice_roll_special = dice_roll in (1, 6)
print(f'Dice rolled: {dice_roll}')
print(f'Special number (1 or 6): {dice_roll_special}')