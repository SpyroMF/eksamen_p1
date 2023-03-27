def sum_partall(liste) -> int:
    # - Debugging -
    # print("[D] Using:",liste)
    # - - - - - - -

    # Produkt will be returned as the sum
    produkt = 0
    for nummer in liste: # Assigns the pointer value to "nummer"
        # - Debugging -
        #
        # print("[D] Pointer:",i)
        # print("[D]   - item:",i)
        # print("[D]   - value:",i%2)
        #
        # - - - - - - -
        if nummer % 2 == 0: # If "nummer" can be divided by two and still be an integer
            
            # - Debugging -
            # print("Appending: ",i)
            # - - - - - - -
            
            produkt += nummer # Adds "nummer" to the "to be returned" produkt variable
    return produkt

def lag_nummerliste() -> list:
    # The "liste" var is going to be returned at the end.
    # It will house all the numbers the user inputs.
    liste = []
    # u_in will house all the temporary inputs from the user.
    u_in = ""
    # While the user input is not "q"
    while u_in.lower() != "q":

        # At the start of ever round, get the user input
        u_in = input("[i] Skriv et nummer (q for å avslutte): ")

        if u_in.lower() == "q":
            return liste

        # To check if the "u_in" has numbers i've created a temp var
        # that is True when "u_in" has numbers and false if it has no
        # numbers.
        u_in_has_symbol: bool = False
        # The for loop checks if symbol (taken from the current pointer
        # of the loop) is or has a number.
        for symbol in u_in: 
            
            # - Debugging -
            # print("[D] Checking if",symbol,"is a number1")
            # - - - - - - -
            

            # If the symbol as a string is a number as a string
            #  - The reason i use strings instead of converting symbol to an int
            #    is that the program crashes if the symbol is a char.
            if symbol in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                
                # - Debugging -
                # print("[D] It is infact a symbol")
                # - - - - - - -

                u_in_has_symbol = True # Set the temp var "u_in_has_symbol" to True
                break # Break (This is done because the symbol var was prooven to have a number)
            # If the symbol var did not turn out as an integer
            else: 
                # - Debugging -
                # print("[D] It is infact not a symbol")
                # - - - - - - -

                u_in_has_symbol = False # Set the temp var "u_in_has_symbol" to False
                break
        
        # If the user input is a number.
        if u_in_has_symbol == True:
            liste.append(int(u_in))
        # If the user input doesn't contain any numbers.
        else:
            print("[E] Husk å bare skriv nummer.")
    
    # - Debugging -
    # print("[D] Returning:", liste)
    # - - - - - - -
    
    # Returns a list of all the numbers the user typed.
    return liste

# Runs the program and prints the length of all the inputed even numbers.
print("[+] Summen er:", sum_partall(lag_nummerliste()))