plaintext = input("Please enter the message you would like to encrypt: ") #obtain a plaintext that is going to be encrypted
key = int(input("Please enter the shift you would like to use ")) #obtain a key shift to use to encrypt the message 

def shift(plaintext, key): #reate a function
    ciphertext = "" #et open string 
    for char in plaintext:
        if char.isupper(): #encrypt uppercase letters 
            ciphertext += chr((ord(char) + key - 65) % 26 + 65) #convert letters to standard cryptography numbers 
        elif char.islower():
            ciphertext += chr((ord(char) + key - 97) % 26 + 97) #convert letters to standard cryptography numbers 
        else: 
            ciphertext += char #if text is not a letter, leave it be 
        

    ciphertext = ciphertext.upper() #convert all letters to uppercase 
    ciphertext = ciphertext.replace(" ", "") #remove spaces 
    return ciphertext 
    
ciphertext = shift(plaintext, key) #set ciphertext to equal the output of the defined function

print("Your encrypted message is", ciphertext) #print results!


