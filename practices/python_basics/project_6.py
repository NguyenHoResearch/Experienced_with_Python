"""-----What will I learn today?-----
- 1. What are function?
- 2. Defining and calling functions.
- 3. Function parameters and arguments.
- 4. Return statement.
- 5. Project 6: Basic math with game.
"""

# %% 1. What are function?
# Functions are reusable blocks of code that perform a specific task.
# They help make code cleaner, modular, and reusable.
# First, to avoid repetition. It means writing once and using many times.
# Second, modularity: it breaks large tasks into smaller ones and, finally, improves readability.
# Additionally, it makes the code easier to understand and maintain when written in functions.

# %% 2. Defining and calling functions.
def function_name():
    # Code block inside the function.
    print("Hello from the function.")

def greet():
    print("Hello, welcome to Python!")

function_name()
greet()

# %% 3. Function parameters and arguments.
def greet_user(name):
    print(f"Hello {name}, Welcome to Python!")

def add(a, b):
    print(f"The sum of {a} and {b} is {a + b}.")

greet_user("Nguyen Ho")
add(9, 10)

# %% 4. Return statement
def multiply(a, b):
    return a * b

x1 = 9
x2 = 10
result = multiply(x1, x2)
print(f"The product of {x1} and {x2} is {result}.")

# %% 5. Project 5: Basic math quiz game.
import random

# Step 1: Define the math question function
def generate_question():
    number_1 = random.randint(1, 10)
    number_2 = random.randint(1, 10)
    operator = random.choice(["+", "-", "*"])

    if operator == "+":
        answer = number_1 + number_2
    elif operator == "-":
        answer = number_1 - number_2
    else:
        answer = number_1 * number_2
    return f"{number_1} {operator} {number_2}", answer

# Step 2: Main Quiz Game Function
def math_quiz():
    score = 0
    rounds = 5

    print("\n--- Welcome to the Math Quiz Game! ---")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for i in range(rounds):
        question, correct_answer = generate_question()
        print(f"\nQuestion {i + 1}: {question}")
        user_answer = int(input("Your answer: "))

        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {correct_answer}")

    print("\n--- Game Over! ---")
    print(f"Your final score is: {score}/{rounds}")
    if score == rounds:
        print("Congratulations! You got all the questions correct.")
    elif score >= rounds // 2:
        print("Good job! You did well.")
    else:
        print("Keep practicing! You can do better next time.")

# Step 3: Run the Game
math_quiz()
# %%
