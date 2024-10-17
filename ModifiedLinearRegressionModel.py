# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 18:31:03 2024

@author: Klaws
"""


import random
import string
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from essential_generators import DocumentGenerator
import re

# %%
gen = DocumentGenerator()
paragraph = gen.paragraph()
paragraph = paragraph.lower()
# %%

#Shift Cipher Encryption
def shift(paragraph, key):
    ciphertext = ""
    for char in paragraph: 
        if char.isalpha():
            ciphertext += chr((ord(char) + key - 97) % 26 + 97)
        else:
            ciphertext += char
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
        paragraph = gen.paragraph() #Get a new quote for every iteration
        paragraph = re.sub(r'[^a-zA-Z]', '', paragraph) #removes non letter characters
        paragraph = paragraph.lower()
        key = random.randint(1, 25)
        ciphertext = shift(paragraph, key)
        frequency_vector_normalized = letterfrequencies(ciphertext)
        dataset.append((frequency_vector_normalized, key))
    return dataset

# %%
#Dataset Generation 
key = random.randint(1,25)
ciphertext = shift(paragraph, key)
dataset = data(1000)
paragraph = paragraph.lower()

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

for i in range(10):
  rounded_prediction = round(y_pred[i]) 
  print(f"Actual shift: {y_test[i]}, Predicted shift: {y_pred[i]:.2f}, Rounded Prediction: {rounded_prediction}")