###
# String manipulation
#

movie = "The Lord of the Rings: The Return of the King"

# print number of characters
print('Number of characters: ', len(movie))

# print title in capital letters
print(movie.upper())

# print title in small letters
print(movie.casefold())

# print how many times the vowel "e" appears in the title
print(f'The letter "e" appears: {movie.count('e')} times')

# print where in the text is the word "Lord"
print(movie.index("Lord"))

# print where in the text is the word "dragon"
print(movie.find("dragon"))