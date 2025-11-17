###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

# determine Celsius degrees value
Celsius = int(input())
# calculate Fahrenheit degrees and Kelvin degrees
Fahrenheit = Celsius * 1.8 + 32
Kelvin = Celsius + 273.15
# Print different types of temperature output
print(Celsius, Fahrenheit, Kelvin)