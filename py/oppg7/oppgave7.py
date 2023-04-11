# This function takes in a string, then opens
# a file, then writes the string to it.
# ----------------------------------------------
# IF THE FILE DOES NOT WORK IT IS IMPORTANT TO 
# RUN IT WITH THE PY/PYTHON COMMAND IN THE FOLDER IT IS.
def write_to_file(string: str):
    file = open("oppgave7.save", "a") # Opens a file as an variable
    file.write(string+"\n") # Writes the choosen string to the file
    file.close # Closes the file
    
def word_count(text: str) -> dict:
    ls = text.split("\n")
    
    tmp_ordliste = {}
    
    # For words in the word list (ls)
    for i in ls:
        # If the words isn't in the dictionary
        if i.lower() not in tmp_ordliste:
            # Add it with the value of 1
            tmp_ordliste[i.lower()] = 1
        # If the word is in the dictionary
        else:
            tmp_ordliste[i.lower()] += 1 # Up the value by 1
    tmp_ordliste.pop("") # Removes the last empty thing
    return tmp_ordliste
        

# Run until stopped.
while True:
    # Take input from the user and assign it to the "i" variable.
    i = input("[i] Skriv ord (q for å avslutte): ")
    
    # If user typed "q", stop the program.
    if i.lower() == "q":
        break

    # Use the write to file functon to save the users supercool words.
    write_to_file(i)

# Runs once for every different word
for key, value in word_count(open("oppgave7.save").read()).items():
    # Prints how many times it has been written
    print("[i] Ordet", key,"ble skrevet", value, "gang(er).")

