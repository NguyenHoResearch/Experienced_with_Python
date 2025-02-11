"""-----What will I learn in this project-----
- 1. What are tuples?
- 2. Tuple operations and unpacking.
- 3. What are Sets?
- 4. Set operations (Union, Intersection, Difference).
- 5. Day 9 Project: Ingredient checker.
"""

# %% 1. What are tuples?
# Tuples are useful for storing fixed collections of items.
# They are an immutable data structure, which means that once created, their contents cannot be changed, 
# added, or removed. Tuples are commonly used for storing fixed collections of items.
"""
my_tuple = (1, 2, 3)
"""
fruits = ("apple", "banana", "cherry")

print(fruits[0])
print(fruits[-1])

coordinates = (10, 20, 30)
x, y, z = coordinates
print(x)
print(y)
print(z)

# %% 2. Tuple operations and unpacking.
fruits = ("apple", "banana", "cherry")
print(len(fruits))

print(fruits + ("orange",))

# %% 3. What are sets?
# A set is an unordered collection of unique items.
# Sets are mutable, but they do not allow duplicates.
"""
my_set = {1, 2, 3}
"""

ingredients = {"flour", "sugar", "butter"}
print(ingredients)

ingredients.add("eggs")
print(ingredients)

ingredients.remove("sugar")
print(ingredients)

# %% 4. Set operations (Union, Intersection, Difference).
set_a = {"flour", "sugar", "butter"}
set_b = {"sugar", "eggs"}

print(set_a | set_b)
print(set_a & set_b)
print(set_a - set_b)

# %% 5. Project 9: Ingredients Checker
# Step 1: Define the recipe ingredients
recipe_ingredients = {"flour", "sugar", "butter", "eggs", "milk"}

# Step 2: Get user input for available ingredients
user_input = input("Enter the ingredients you have (separated by commas): ")
user_ingredients = set(user_input.split(", "))

# Step 3: Compare Ingredients
missing_ingredients = recipe_ingredients - user_ingredients
extra_ingredients = user_ingredients - recipe_ingredients

# Step 4: Display Results
print("\n--- Ingredient Check Results ----")
if missing_ingredients:
    print(f"You are missing the following ingredients: {', '.join(missing_ingredients)}")
else:
    print("You have all the ingredients needed.")

if extra_ingredients:
    print(f"You have extra ingredients: {', '.join(extra_ingredients)}")
else:
    print("You have all the ingredients needed.")