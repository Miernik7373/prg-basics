computer_science = input("Are you interested in computer science? (y/n): ")
games = input('Do you like playing computer games? (y/n): ')
instagram = input("Do you have an Instagram account? (y/n): ")
if computer_science == 'y':
    answer_1 = "Yes"
else:
    answer_1 = "No"
if games == 'y':
    answer_2 = "Yes"
else:
    answer_2 = "No"
if instagram == 'y':
    answer_3 = "Yes"
else:
    answer_3 = "No"
print("SURVEY RESULTS:")
print(f'Interested in computer science: {answer_1}')
print(f'Playing computer games: {answer_2}')
print(f'Has an Instagram account: {answer_3}')
