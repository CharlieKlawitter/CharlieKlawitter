import random  as random 
import pyquotegen

# %%

#Shift Cipher Encryption
def shift(quote, key):
    ciphertext = ""
    for char in quote:
        ciphertext += chr((ord(char) + key - 97) % 26 + 97)
       
    ciphertext = ciphertext.upper()

    return ciphertext

#Generate Encrypted Data

def data(quote, num_samples=1000):
    dataset = []
    for _ in range(num_samples):
        quote = pyquotegen.get_quote() #Get a new quote for every iteration
        quote = quote.replace("," , "").replace('.' , "").replace("'" , "").replace(" ", "") #Clean up quote 
        quote = quote.lower() #
        key = random.randint(1, 25)
        ciphertext = shift(quote, key)
        dataset.append((quote, ciphertext, key))
    return dataset


 
# %%
#Dataset Generation 
key = random.randint(1,25)
ciphertext = shift(quote, key)
dataset = data(quote, 1000)
quote = quote.lower()

print(dataset[:5])
