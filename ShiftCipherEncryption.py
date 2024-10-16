plaintext = input("Please enter the message you would like to encrypt: ")
key = int(input("Please enter the shift you would like to use "))

def shift(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char.isupper():
            ciphertext += chr((ord(char) + key - 65) % 26 + 65)
        elif char.islower():
            ciphertext += chr((ord(char) + key - 97) % 26 + 97)
        else: 
            ciphertext += char

    ciphertext = ciphertext.upper()

    return ciphertext 
    
ciphertext = shift(plaintext, key)

print("Your encrypted message is", ciphertext)

