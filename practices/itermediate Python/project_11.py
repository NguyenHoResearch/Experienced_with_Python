"""-----What will I learn in this project-----
- 1. What are exceptions?
- 2. Using try, except, else, and finally.
- 3. Handling multiple exceptions.
- 4. Raising custom exceptions.
- 5. Project 11: safe calculator.
"""

# %% 1. What are exceptions?
# Exceptions are errors that occur during the execution of a program, disrupting its normal flow.
# Some common Python exceptions include the ValueError, which is raised when an operation 
# receives an argument of the correct type but with an inappropriate value.
# Then, we have the ZeroDivisionError, which is raised when dividing by zero.
# We also have the TypeError, which is raised when an operation is performed on an inappropriate data type.
# Finally, we have the FileNotFoundError, which we have already used. It is raised when a file operation fails because the file does not exist.
try:
    num = int(input("Enter a number:"))
    result = 10 / num
    print("Result: ", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")


# %% 2. Using try, except, else, and finally.
"""
try:
  # Code that might raise an exception
except ExceptionType:
  # Code to handle the exception
else:
  # Execute if no exception occurs
finally:
  # Always execute, even if an exception occurs
"""

try:
    num = int(input("Enter a number:"))
    result = 10 / num
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print("No exception occurred. Result: ", result)
finally:
    print("Finally block executed. Program Ended")

# %% 3. Handling multiple exception.
try:
    num = int(input("Enter a number:"))
    result = 10 / num
except (ZeroDivisionError, ValueError):
    print("Error: Division by zero or Invalid Input")

# %% 4. Raising custom exception. 
def withdraw(amount):
    if amount < 0:
        # In Python, the raise keyword is used to manually trigger 
        # an exception. This allows you to create custom error messages and handle exceptions in a controlled way.
        raise ValueError("Invalid withdrawal amount - Amount cannot be negative")
    print(f"You have withdrawn ${amount}")

try:
    withdraw(-50)
except ValueError as e:
    print(e)

# %% 5. Project 11: Safe calculator
# Step 1: Define Calculator Functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y

# Step 2: Display Menu
def show_menu():
    print("\n--- Safe Calculator Menu ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

# Step 3: Main Program
while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '5':
        print("Exiting the calculator. Goodbye!")
    break

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
      print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    else:
        print("Invalid choice. Please select a valid option.")

except ValueError:
    print("Invalid input. Please enter valid numbers.")
except ZeroDivisionError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("Thank you for using the Safe Calculator!... Restarting...")
# %%
