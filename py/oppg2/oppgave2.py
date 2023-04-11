
# Function which will take in a string and return the number of words as an integer.
def get_word_count(string: str) -> int:
    # Uses the built-in .split function that returns a list.
    # For each space it will splitt the word and add it into the "words" variable 
    words = string.split(" ", -1)
    # For words
    
    produkt = 0
    for word in words:
        # If the word that is pointed to has fewer than 3 symbols [0, 1, 2, 3] (Easier explained as less than 4 letters)
        # then it will add 1 to the temp value "produkt" which should be returned
        if len(word) > 3:
            produkt += 1
    # Returns the amount of words that is larger than 3 words
    return produkt

# Uses the get_word_coundt function and user input and prints 
# the number of words in the inputed string.
print(
    "Antall ord i settningen:",
    get_word_count(input("Skriv en settning:\n"))
)