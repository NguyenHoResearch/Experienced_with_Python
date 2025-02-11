"""-----What will I will learn in project 2-----
- 1. What are variables?
- 2. Data Types: Strings, Integers, Floats, and Booleans.
- 3. Type Conversion:
- 4. String Formatting
- 5. Project 2: Personalized Greeting Program
"""
# %% 1. What's is variables?
"""A variable is like a container where you can 
    store data such as names, numbers, or even calculations."""

# Storing a name in variables.
# They must begin with a letter or an underscore and are CaSe SeNsItIve. 
# Additionally, some words are reserved in Python and so cannot be used for variable names (e.g. import or for).
name = "name - Nguyen Ho" 
Name = "Name - Nguyen Ho"
name1 = "name1 - Nguyen Ho"
Name1 = "Name1 - Nguyen Ho"
myname = "myname - Nguyen Ho"
myName = "myName - Nguyen Ho"
_name = "_name - Nguyen Ho"
name_ = "name_ - Nguyen Ho"
print(f"\n{name}, \n{Name}, \n{name1}, \n{Name1}, \n{myname}, \n{myName}, \n{_name}, \n{name_}")

# Illegal variable names
# name: = "name: - Nguyen Ho"
# 1Name = "1X - Nguyen Ho"
# Name-1 = 1
# for = 1

# Storing an age in variables.
age = 18
print(age)

# %% 2. Data types: Strings, Integers, Floats, and Booleans. 
# Python has different data types for storing different types of information.
# The different ones that we know are strings, which actually have text enclosed in quotes.
# We have integers which are whole numbers.
# We have float which are decimal numbers.
# we have boolean which are true and false values.

# String
name = "Nguyen Ho"

# Integer
age = 18

# Float
height = 1.77

# Boolean
is_student = True

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))
# %% 3. Type conversion
# Now, sometimes we need to convert one data type into another.

# A string into an interger, float, or bool.
age = "18"
myAgeInt = int(age)
myAgeFloat = float(age)
myAgeBool = bool(age)

print(myAgeInt + 5)
print(myAgeFloat + 5)
print(myAgeBool + 5)

# %% 4. String formating
# Three main ways to format strings in Python.

name = "Nguyen Ho"
# The first way:
print("Hello, " + name + "!")

# The second way:
print("Hello, {}!".format(name))

# The third way:
print(f"Hello, {name}!")

# %% 5. Project 2: Personalized greeting program.
# Step1: Ask for user details
name = input("What's your name? ")
age = int(input("How old are you? "))
color = input("What's your favorite color?  ")

# Step2: Gennerate a personalized greeting message.
print("\n-----Persionalized Greeting-----")
print(f"Hello, {name}!")
print(f"You are {age} years old and {color} is a beautiful color.")
print("You are now ready start your Python adventure 🐍.")
