#!/usr/bin/python3
# inputs from the user
input_string = input("Enter the text to be ciphered/decipherd:\n")
# the inputted string can not contain ! mark
# Because it is interpreted as signature sign
# the next letter after ! mark will be read as a non ciperable character
# it will be used to pass the cipher algorithm and decipher methods
# k indicates it has been ciphered with "KINU" by Shayikh Mostofa
# if you invent more cipher algorithm then please include them in the signature
# database and update the code accordingly before use
signature_database = [
    "k",
    "z"
]
signature_valid = False
signature_found = False
class signature_not_found_error(Exception):
    def __init__(self):
        pass
class invalid_signature(Exception):
    def __init__(self):
        pass
class invalid_data(Exception):
    def __init__(self):
        pass
for i in range(int(len(input_string))):
    if input_string[i] == "!":
        signature = input_string[i+1]
        print("Signature found: " + signature)
        signature_found = True
        break
try:
    if not signature_found:
        raise signature_not_found_error
    for i in range(len(signature_database)):
        if signature_database[i] == signature:
            signature_valid = True
    for i in range(len(input_string)):
        if input_string[i] == "!":
            try:
                if input_string[i+2]:
                    raise invalid_data
            except IndexError:
                pass
            except invalid_data:
                print("Invalid syntax of the cipherable text")
                print("Exiting...")
                exit()
    if not signature_valid:
        raise invalid_signature
except signature_not_found_error:
    print("Signature not found invalid data")
    print("Exiting...")
    exit()
except invalid_signature:
    print("Signature does not exist in the database")
    print("Exiting...")
    exit()

# Main Code Entry
# declare ciphered text
ciphered_text = ""
if signature == "k":
    #code
    for i in range(len(input_string)):
        if input_string[i].isalpha():
            if input_string[i] == "a":
                ciphered_text += "i"
            elif input_string[i] == "b":
                ciphered_text += "h"
            elif input_string[i] == "c":
                ciphered_text += "g"
            elif input_string[i] == "d":
                ciphered_text += "f"
            elif input_string[i] == "e":
                ciphered_text += "y"
            elif input_string[i] == "f":
                ciphered_text += "d"
            elif input_string[i] == "g":
                ciphered_text += "c"
            elif input_string[i] == "h":
                ciphered_text += "b"
            elif input_string[i] == "i":
                ciphered_text += "a"
            elif input_string[i] == "j":
                ciphered_text += "r"
            elif input_string[i] == "k":
                ciphered_text += "q"
            elif input_string[i] == "l":
                ciphered_text += "p"
            elif input_string[i] == "m":
                ciphered_text += "o"
            elif input_string[i] == "n":
                ciphered_text += "z"
            elif input_string[i] == "o":
                ciphered_text += "m"
            elif input_string[i] == "p":
                ciphered_text += "l"
            elif input_string[i] == "q":
                ciphered_text += "k"
            elif input_string[i] == "r":
                ciphered_text += "j"
            elif input_string[i] == "s":
                ciphered_text += "x"
            elif input_string[i] == "t":
                ciphered_text += "w"
            elif input_string[i] == "u":
                ciphered_text += "v"
            elif input_string[i] == "v":
                ciphered_text += "u"
            elif input_string[i] == "w":
                ciphered_text += "t"
            elif input_string[i] == "x":
                ciphered_text += "s"
            elif input_string[i] == "y":
                ciphered_text += "e"
            elif input_string[i] == "z":
                ciphered_text += "n"  
        elif input_string[i].isdigit():
            if input_string[i] == "0":
                ciphered_text += "8"
            elif input_string[i] == "1":
                ciphered_text += "5"
            elif input_string[i] == "2":
                ciphered_text += "7"
            elif input_string[i] == "3":
                ciphered_text += "9"
            elif input_string[i] == "4":
                ciphered_text += "6"
            elif input_string[i] == "5":
                ciphered_text += "1"
            elif input_string[i] == "6":
                ciphered_text += "4"
            elif input_string[i] == "7":
                ciphered_text += "2"
            elif input_string[i] == "8":
                ciphered_text += "0"
            elif input_string[i] == "9":
                ciphered_text += "3"
        else:
            ciphered_text += input_string[i]

print(ciphered_text)





    



