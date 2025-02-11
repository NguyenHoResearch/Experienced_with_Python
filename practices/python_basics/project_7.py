"""-----What will I learn in this project-----
- 1. What are lists?
- 2. Lists operators: Adding, remove, accessing items.
- 3. Looping throung lists.
- 4. List methobs
- 5. Project 7: Shoping list app
"""
# %% 1. What are lists?
# A list is a collection of items stored in a single variable.
# Lists are ordered, which means items have a specific sequence.
# They are mutable, which means you can change, add, or remove items 
# and they are indexed, which means each item has an Has an index starting at zero.

shopping_list = ["Milk", "Eges", "Bread"]
print(shopping_list)
# %% 2. Lists operators: adding, remove, accessing items.
shopping_list = ["Milk", "Eges", "Bread"]
print(shopping_list[1])

shopping_list.append("Fruits")
shopping_list.insert(1, "Juices")
print(shopping_list)

shopping_list.remove("Juices") 
print(shopping_list)

shopping_list.pop() # Delete the final element or delete the element in the position.
print(shopping_list)

# %% 3. Looping through lists.
shopping_list = ["Milk", "Eges", "Bread"]

# Case 1:
for item in shopping_list:
    print(f"-{item}")

# Case 2:
for index, item in enumerate(shopping_list): # Enumerate for lists, tubles, strings, ...
    print(f"{index + 1}: {item}")

# %% 4. Lists methobs.
shopping_list = ["Milk", "Eges", "Bread"]
print(shopping_list)

shopping_list.sort()
print(shopping_list)

shopping_list.reverse()
print(shopping_list)

shopping_list.clear()
print(shopping_list)

# %% 5. Project 7: Shopping lists app.
# Step 1: Initialize an empty shopping list
shopping_list = []

# Step 2: Define the main menu
def show_menu():
  print("\n--- Shopping List Menu ---")
  print("1. View the shopping list")
  print("2. Add an item")
  print("3. Remove an item")
  print("4. Clear List")
  print("5. Exit")

# Step 3: Main Program Loop
while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        print("\n--- Shopping List ---")
        if not shopping_list:
            print("Your shopping list is empty.")
        else:
            for index, item in enumerate(shopping_list):
                print(f"{index + 1}. {item}")

    elif choice == "2":
        item = input("Enter the item to add: ")
        shopping_list.append(item)
        print(f"{item} has been added to the shopping list.")

    elif choice == "3":
        item = input("Enter the item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} has been removed from the shopping list.")
        else:
            print(f"{item} is not in the shopping list.")

    elif choice == "4":
        shopping_list.clear()
        print("The shopping list has been cleared.")

    elif choice == "5":
        print("Goodbye! Happy Shopping!")
        break
    else:
        print("Invalid choice. Please try again.")
