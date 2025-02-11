"""-----What will I lean to this project-----
- 1. What are If-Else statements?
- 2. Comparison operators.
- 3. Logical operators.
- 4. Nested If-Else statements.
- 5. Project 4: Number comparison tool.
"""

# %% 1. What are If-Else statements?
"""
if condition:
    # Do something if the condition is true.
else:
    # Do some thing if the condition is Fales.
"""
number = 10
if number > 5:
    print("The number is great than 5.")
elif number == 5:
    print("The number is equal 5.")
else:
    print("The number is less than 5.")

# %% 2. Comparison operators.
# Comparison operators are used to compare values in an if statement.
# Can compare equal to not equal, to greater than less than, greater than or equal, to less than or equal to.
number = 5
if number == 5:
    print("The number is equal 5.")
if number != 5:
    print("The number is not equal 5.")

if number >= 5:
    print("The number is great or equal 5.")
else:
    print("The number is less or equal 5. ")

# %% 3. Logical operators.
"""
Keyword (Scalar)    Function        Bitwise     True if ...
and                 logical_and     &           Both True
or                  logical_or      or          Either or Both True
not                 logical_not     not         Not True
XOR                 logical_xor     ^           One True and One False
"""

a = 7
b = 20

print("\n----- Logical operator: and -----")
if a > 5 and b < 15:
    print("Both conditions are true.")
else:
    print("At least one condition is false.")

print("\n----- Logical operator: or -----")
if a > 5 or b < 15:
    print("At least one condition is true.")
else:
    print("Both conditions are false.")

print("\n----- Logical operator: not -----")
if not((a > 5) and (b < 15)):
    print("One or two conditions are false.")
else:
    print("Both conditions are true.")

print("----- Logical operator: XOR -----")
if (a > 5) ^ (b < 15):
    print("Only one condition true.")
else:
    print("Both condictions is true or flase.")

# %% 4. Nested If-Else statements.
number = 10
if number > 5:
    print("The number is great than 5.")
elif number == 5:
    print("The number is equal 5.")
elif number == 6:
    print("The number is equal 6.")
else:
    print("The number is less than 5.")

# %% 5. Project 4: Number comparison tool.

# Step 1: Get user input for two numbers
number_1 = float(input("Enter the first number: "))
number_2 = float(input("Enter the second number: "))

# Step 2: Compare the numbers
print("\n--- Comparison Results ----")
if number_1 == number_2:
    print(f"Both numbers are equal: {number_1}")
elif number_1 > number_2:
    print(f"{number_1} is greater than {number_2}")
else:
    print(f"{number_1} is greater than {number_1}")

# Step 3: Check if any number is zero
if number_1 == 0 or number_2 == 0:
    print("\nAt least one number is zero.")
else:
    print("\nBoth numbers are non-zero.")

# %%
