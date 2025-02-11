"""-----What will I learn in this project-----
- 1. What are loops?
- 2. For loop.
- 3. While loop.
- 4. Using time.sleep() for deplays.
- 5. Project 5: Countdown Timer.
"""

# %% 1. What are loops
# Loops are used to repeat a block of code multiple times.
# There are two main types of loops in Python.
# First one is the for loop, which repeats a set number of times,
# Second the while loop which repeats until a condition becomes false.

""" 
for item in interable:
    # Code to run
"""

"""
while logical:
    # Code to run
    # Update logical 
"""

# %% For loop
print("\n-----Case 1: Use the for loop.-----")
for i in range(5):
    print(i)

print("\n-----Case 2: Use the for loop.-----")
for i in range(1, 5):
    print(i)

print("\n-----Case 3: Use the for loop.-----")
for i in range(5, 2, -1):
    print(i)

# %% While loop
count = 5

print("-----Use the while loop.-----")
while count > 0:
    print(count)
    count -= 1

# %% Using time.sleep() for Deplays
import time

print("\n-----Case 1: Use the for loop.-----")
for i in range(5):
    print(i)
    time.sleep(1)
print("🎆Happy New Year🎆")

print("\n-----Case 2: Use the for loop.-----")
for i in range(1, 5):
    print(i)
    time.sleep(1)
print("🎆Happy New Year🎆")


print("\n-----Case 3: Use the for loop.-----")
for i in range(5, 2, -1):
    print(i)
    time.sleep(1)
print("🎆Happy New Year🎆")
# %% 5. Project 5: Countdown Timer.
import time

# Step 1: Get user input for the countdown start.
start = int(input("Enter the number of countdown start here: "))

# Step 2: Countdown using a while loop.
print("-----Countdown Begin-----")
while start >= 0:
    print(start)
    start -= 1
print("Coundouwn Complate!")
# %%
