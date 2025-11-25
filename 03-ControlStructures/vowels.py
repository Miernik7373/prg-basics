###
# Counts vowels in the text
#
text = "This text has got eight vowels."
vowels = "aeiouAEIOU"
vowel_count = 0

# Count vowels in the text
for char in text:
    if char in vowels:
        vowel_count += 1

print(f"The number of vowels in the text is: {vowel_count}")



