
import random
import pyquotegen
import string
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np
from sklearn.preprocessing import PolynomialFeatures


# %%
quote = pyquotegen.get_quote()
quote = quote.lower()
# %%

#Shift Cipher Encryption
def shift(quote, key):
    ciphertext = ""
    for char in quote: 
            ciphertext += chr((ord(char) + key - 97) % 26 + 97)
     
    ciphertext = ciphertext.upper()
    return ciphertext

def letterfrequencies(ciphertext):
    frequency_vector = {char: 0 for char in string.ascii_lowercase}
    
    for char in ciphertext:
        if char.isalpha():
            frequency_vector[char.lower()] += 1

    # Normalize frequencies and create a dataset of letter-frequency pairs
    total_letters = sum(frequency_vector.values())
    frequency_data = []
    
    for char in string.ascii_lowercase:
        frequency_data.append(frequency_vector[char] / total_letters if total_letters > 0 else 0)

    return frequency_data 
#Generate Encrypted Data

def data(num_samples=1000):
    dataset = []
    for _ in range(num_samples):
        quote = pyquotegen.get_quote() #Get a new quote for every iteration
        quote = quote.replace("," , "").replace('.' , "").replace("'" , "").replace(" ", "")
        quote = quote.lower()
        key = random.randint(1, 25)
        ciphertext = shift(quote, key)
        frequency_vector_normalized = letterfrequencies(ciphertext)
        dataset.append((frequency_vector_normalized, key))
    return dataset

# %%
#Dataset Generation 
key = random.randint(1,25)
ciphertext = shift(quote, key)
dataset = data(1000)
quote = quote.lower()

print(dataset[:5])

# %%

X = np.array([item[0] for item in dataset])
y = np.array([item[1] for item in dataset])
# %%

#Test/TrainSplit
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# %% 

#Linear Regression Model 

model = LinearRegression()
model.fit(X_train, y_train)

# %%

# Make predictions

y_pred = model.predict(X_test)

# %%

# Evaluate the model 

mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squares Error: {mse}")


# %%

# Display some predicitions 

for i in range(5):
  rounded_prediction = round(y_pred[i]) 
  print(f"Actual shift: {y_test[i]}, Predicted shift: {y_pred[i]:.2f}, Rounded Prediction: {rounded_prediction}")