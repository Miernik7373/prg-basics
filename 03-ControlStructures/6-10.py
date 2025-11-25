human_age = int(input("Enter human years: "))
dog_age = 0
dog_age_above_two = 21
for i in range(human_age):
    if human_age <=2:
        dog_age += 10.5
    else: 
        dog_age = dog_age_above_two - 4
        dog_age_above_two += 4
print(f"The dog's age in dog's years is {dog_age} years.")