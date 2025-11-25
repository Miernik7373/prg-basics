age = int(input("Write your age: "))
age_group = "Huh?"
if 0<=age<13:
    age_group = "Child"
elif 12<age<20:
    age_group = "Teen"
elif 19<age<65:
    age_group = "Adult"
elif 64<age<120:
    age_group = "Senior"
elif 119<age:
    age_group = "Dead XD"
print(f'Your age group is: {age_group}')