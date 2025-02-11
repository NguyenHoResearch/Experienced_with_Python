
"""-----What will I learn in project 1.-----
- 1. What is a print statement?
- 2. How to use print with text and number?
- 3. String formatting for dynamic messages.
- 4. Using user input with print.
- 5. Project 1: Welcome Message Generator.
"""

#%% 1. What is a print statement?
"""The print statement is Python's most basic way 
    to display output on the screen."""

print("Hello, Python World!")

#%% 2. How to use print text and number?
print("The number is", 10)
print("5 + 5 =",5 + 5)

#%% 3. String formatting for dynamic messages
name = "Nguyen Ho"
print(f"Hello, {name}! Wellcome to Python programing.")

#%% 4. Using user input with print.
userName = input("What's your name? ")
print(f"Hello, {userName}! Welcome to Python programing.")

#%% 5. Project 1: Welcome Message Generator
# Step 1: ask for user detail
name = input("What's your name? ")
hobby = input("What your favorite hobby? ")

# Step 2: generate a personalized welcome message
print("\n-----Welcome Message-----")
print(f"Hello, {name}!👋")
print("Welcome to the world of Python programing.")
print(f"It's great to know that you love {hobby}.")
print("Get ready to build something amazing today.")