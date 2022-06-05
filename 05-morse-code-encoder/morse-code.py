# --- Import the list of character to morse code codes:
from morse_code_codes import morse_codes


def encode(word, list_of_letters):
    """Create a list of morse code encoded characters from a list of letters."""
    
    # --- Create an empty list:
    morse_coded_word = []
    
    # --- Cycle through each letter and append the resulting morse code to the morse_coded_word list:
    for item in list_of_letters:
        if item in morse_codes:
            morse_coded_word.append(morse_codes[item])
    
    # --- Return the morse_coded_word list back to the user_entry function:
    return morse_coded_word


def user_entry():
    """Ask the user for some words to encode and then call the encode function and print out the resulting morse coded letters."""
    
    word = input("Enter a word: ").upper()
    
    # --- Convert the words the user inputs into a list:
    list_of_letters = list(word)
    
    # --- Print the list of letters:
    print(list_of_letters)
    
    # --- Print the morse code encoded characters as a list:
    print(encode(word = word, list_of_letters = list_of_letters))

# --- Start the program:
if __name__ == "__main__":
    user_entry()