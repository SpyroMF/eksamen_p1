# This function takes in a string, then opens
# a file, then writes the string to it.
# ----------------------------------------------
# IF THE FILE DOES NOT WORK IT IS IMPORTANT TO 
# RUN IT WITH THE PY/PYTHON COMMAND IN THE FOLDER IT IS.
def write_to_file(string: str):
    file = open("oppgave7.save", "a") # Opens a file as an variable
    file.write(string+"\n") # Writes the choosen string to the file
    file.close # Closes the file
    
def word_count(text: str):
    strings = text.split(" ")
    

# Run until stopped.
while True:
    # Take input from the user and assign it to the "i" variable.
    i = input("[i] Skriv ord (q for å avslutte): ")
    
    # If user typed "q", stop the program.
    if i.lower() == "q":
        break

    # Use the write to file functon to save the users supercool words.
    write_to_file(i)

