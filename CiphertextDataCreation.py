import random  as random 

#Shift Cipher Encryption
def shift_cipher_encrypt(plaintext, key): 
    ciphertext = "" 
    for char in plaintext:
        if char.isupper(): 
            ciphertext += chr((ord(char) + key - 65) % 26 + 65) 
        elif char.islower():
            ciphertext += chr((ord(char) + key - 97) % 26 + 97) 
        else: 
            ciphertext += char 
        

    ciphertext = ciphertext.upper() 
    ciphertext = ciphertext.replace(" ", "")  
    return ciphertext 
    
#Generate Encrypted Data

def data(text, num_samples=1000):
    dataset = []
    for _ in range(num_samples):
        key = random.randint(0, 25)
        ciphertext = shift_cipher_encrypt(text, key)
        dataset.append((ciphertext, key))
    return dataset

#Dataset Generation 

plaintext = "This is an example of shift cipher encryption to generate a data set"
dataset = data(plaintext, 1000)

print(dataset[:5])
