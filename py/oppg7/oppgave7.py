from cryptography.fernet import Fernet

# thanks https://stackoverflow.com/questions/2490334/simple-way-to-encode-a-string-according-to-a-password
def encrypt(message: bytes, key: bytes) -> bytes:
    return Fernet(key).encrypt(message)

def decrypt(token: bytes, key: bytes) -> bytes:
    return Fernet(key).decrypt(token)

# This function takes in a string, then opens
# a file, then writes the string to it.
# ----------------------------------------------
# IF THE FILE DOES NOT WORK IT IS IMPORTANT TO 
# RUN IT WITH THE PY/PYTHON COMMAND IN THE FOLDER IT IS.
def write_to_file(string: str):
    file = open("oppgave7.save", "ab") # Opens a file as an variable

    key = open("oppgave7.key", "r").read()
    print("Key:",key) # Debug
    token = encrypt(bytes(string, encoding="utf8"), key)
    file.write(token+"\n".encode()) # Writes the choosen string to the file
    file.close # Closes the file

def get_file_content():
    key = open("oppgave7.key", "r").read
    oppg7 = open("oppgave7.save", "r").read
    oppg7raw = decrypt(oppg7, key)
    print(oppg7raw)



def gen_key():
    file = open("oppgave7.key", "wb")
    file.write(Fernet.generate_key())

def word_count(text: str):
    strings = text.split(" ")
    for word in strings:
        pass
    

# Generate key
gen_key()
# Run until stopped.
while True:
    # Take input from the user and assign it to the "i" variable.
    i = input("[i] Skriv ord (q for å avslutte): ")
    
    # If user typed "q", stop the program.
    if i.lower() == "q":
        break

    # Use the write to file functon to save the users supercool words.
    write_to_file(i)

get_file_content()
