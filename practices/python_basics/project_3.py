"""-----What will I learn in project 3-----
- 1. User input with input.
- 2. Type conversion (int() and float()).
- 3. String formatting with f-strings.
- 4. Basic arithmetic operations.
- 5. Project 3: Simple calculator.

"""
# %% 1. User input with input
# The input function allows users to type values into the program.
name = input("Enter your name: ")
print(f"Hello, {name}")

# %% 2. Type conversion (int() and float()
number_int = int(input("Enter an integer here: "))
number_float = float(input("Enter a float here: "))
number_str = str(number_int)

print(number_int)
print(number_float)
print(number_str * 2)


# %% 3. String formatting with f-strings
number_1 = int(input("Enter the first integer here: "))
number_2 = int(input("Enter the second integer here: "))
result = number_1 + number_2

print(f"The sum of two numbers, {number_1} and {number_2}, is {result}.")
# %% 4. Basic arithmetic operations.
x = 20
y = 10

print(f"Addition: {x + y}")
print(f"Subtraction: {x - y }")
print(f"Multiplication: {x * y}")
print(f"Division: {x / y}")
print(f"Floor division: {x // y}")
print(f"Modulus: {x % y}")
print(f"Exponentiation:  {x ** y}")

# %% 5. Project 3: Simple calculator.
# Step 1: Get user input for two number.
number_1 = float(input("Enter the first number: "))
number_2 = float(input("Enter the second number: "))

# Step 2: Perform arithmetic operation
addition = number_1 + number_2
subtraction = number_1 - number_2
multiplication = number_1 * number_2
division = number_1 / number_2

# Step 3: Display the result
print("-----Operator Results-----")
print(f"Addition: {number_1} + {number_2} = {addition}")
print(f"Subtraction: {number_1} - {number_2} = {subtraction}")
print(f"Multiplication: {number_1} x {number_2} = {multiplication}")
print(f"Division: {number_1} / {number_2}= {division}")
