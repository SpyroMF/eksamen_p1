
# Function which will take in a string and return the number of words as an integer.
def get_word_count(string: str) -> int:
    # Uses the built-in .split function that returns a list.
    # For each space it will splitt the word and add it into the "words" variable 
    words = string.split(" ", -1)
    # Retrurns the length of the word
    return len(words)

# Uses the get_word_coundt function and user input and prints 
# the number of words in the inputed string.
print(
    "Antall ord i settningen:",
    get_word_count(input("Skriv en settning:\n") + 1)
)