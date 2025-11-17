###
# Calculation of circle area and circumference 
#

# determine radius and PI values
radius = int(input())
PI = 355/113
# calculate area 
area = radius**2*PI
# calculate circumference 
circumference = radius*2*PI
# print results
print(f'{area}, {circumference}')