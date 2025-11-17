###
# A program that prints your height both in cm and in feet and inches.
#
cm = int(input())
feet= int(cm/30.48)
inches = cm%3
# calculate the number of feet

print(f'I am {cm}cm tall, i.e. {feet} feet and {inches} inches'