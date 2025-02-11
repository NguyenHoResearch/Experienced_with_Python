"""----What will you learn in this project-----
- 1. What are modules and libraries?
- 2. Importing modules.
- 3. Built-in Python libraries.
- 4. Creating and using custom modules.
- 5. Project 14: Random password generator.
"""
# %% 1. What are modules and libraries?
# A module is a Python file containing functions, classes, and variables you can reuse in code.
import math

print(math.sqrt(16))

# %% 2. Importing modules.

from random import *
from random import choices

print(randint(1, 10))

print(choices(["Apple", "Banana", "Cherry"]))

# %% 3. Built-in Python Libraries.

import random

password = "".join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=10))
print(password)

#%% 4. Creating using and custom modules.
import greetings
print(greetings.say_hello("John"))

# %% 5. Project 14: Random password generator.
import random, string
# Step 1: Define Password Generation Function
def generate_password(length=12):
  if length < 4:
    raise ValueError("Password length must be at least 4 characters")

  # Character sets for the password
  uppercase = string.ascii_uppercase
  lowercase = string.ascii_lowercase
  digits = string.digits
  special_chars = "!@#$%^&*()_+-=[]{}|;:',.<>?/"

  # Ensure at least one of each character type
  password = [
      random.choice(uppercase),
      random.choice(lowercase),
      random.choice(digits),
      random.choice(special_chars)
  ]

  # Fill the remaining length with random choices from all sets
  all_chars = uppercase + lowercase + digits + special_chars
  password += random.choices(all_chars, k=length - 4)

  # Shuffle the password to make it more random
  random.shuffle(password)

  # Convert the list to a string and return
  return ''.join(password)

# Step 2: User Interaction
try:
  length = int(input("Enter the desired password length (minimum 4): "))
  password = generate_password(length)
  print("Generated Password:", password)
except ValueError as e:
  print(e)

# %%
