# Ask the user to enter a word
user_word = input("Enter a word: ")

# Convert the word to uppercase
user_word = user_word.upper()

# Initialize an empty string to store the uneaten letters
uneaten_letters = ""

# Iterate through each character in the word
for letter in user_word:
    # Check if the letter is a vowel (A, E, I, O, U)
    if letter in "AEIOU":
        # If it's a vowel, continue to the next iteration to skip it
        continue
    # If it's not a vowel, add it to the uneaten_letters
    uneaten_letters += letter

# Print the uneaten letters on separate lines
for letter in uneaten_letters:
    print(letter)
