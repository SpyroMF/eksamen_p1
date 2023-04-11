
# A function that returns a list of words typed by the user
def make_word_list() -> list:
    # word list will contain all the typed words.
    word_list = []

    # A while loop that must be stopped from the inside
    while True:
        # Takes in user input
        user_input = input("[i] Skriv inn et ord (q for å avslutte): ")
        
        # If the user typed q, then return the word list.
        if user_input == "q":
            return word_list
        # If the user used a space, send an error message.
        if " " in user_input:
            print("[!] Det var for mange ord! :(")
        # If the user didn't use a space, add the typed word.
        else:
            word_list.append(user_input)

# This function will find the longest word and return it
def find_longest_word(strings: list) -> int:

    # This counter keeps track of the longest word
    counter = 0

    # Runs of every word in the refered list
    for word in strings:

        # If the word is longer than counter, then set counter to be
        # equal to the word length
        if len(word) > counter:
            counter = len(word)
    # Return the length of the longest word
    return counter

def find_shortest_word(strings: list) -> int:
    # This counter keeps track of the shortest word
    counter = find_longest_word(strings)

    # Runs of every word in the refered list
    for word in strings:

        # If the word is shorter than counter, then set counter to be
        # equal to the word length
        if len(word) < counter:
            counter = len(word)
    # Return the length of the shortest word
    return counter

# Runs the program and prints the longest word
print(
    "[i] Lengded på det minste ordet var:",
    find_shortest_word(make_word_list())
)