#%% Exercise 1: Write a program in Python to display the Factorial of a number.

factorial = 5 * 4 * 3 * 2 * 1 

print(factorial)
#%% Exercise 2: Write a program in Python to reverse a word.
word = "Think python."

reverse_word = word[::-1]
reverse_word
#%% Exercise 3: Write a Python program to reverse a number.
number = 1234

reverse_number = int(str(number)[::-1])
reverse_number

#%% Exercise 4: Write a program to print n natural numbers in descending order using a while loop.
natural_number = 5

while natural_number >= 0:
    print(natural_number)
    natural_number -= 1

#%% Exercise 5: Write a program to display the first 7 multiples of 7.

# Step 1: Initialize default variables.
number = 7
result = 0

# Step 2: Display the first 7 multiples 7.
print(f"\n-----The First 7 Multiples Of 7--------")
for i in range(1, number + 1):
    result = number * i
    print(f"\n7 X {i} = {result}")

#%% Exercise 6: Write a program that appends the square of each number to a new list.

#Step 1: Initialize default variables.
list_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = []

#Step 2: Appends the square of each number to a new list.
for i in list_numbers:
    new_list.append(i ** 2)

#print(new_list)

#%% Exercise 7: WAP to separate positive and negative numbers from a list.

# Step 1: Initialize
list_numbers = [1, -2, 3, -4, 5, 6, -7, -8, -9, 10]
list_positive_numbers = []
list_negative_numbers = []
neutral_numbers = []


# Step 2: Separate positive and negative numbers from a list.
for i in list_numbers:
    if i == 0:
        print("In the list, there is a neotral(0) number.")

    if i < 0:
        list_negative_numbers.append(i)
    else:
        list_positive_numbers.append(i)

print(list_positive_numbers)
print(list_negative_numbers)

#%% Exercise 8: Write a program that appends the type of elements from a list.


#%% Exercise 9: Write a program to filter even and odd numbers from a list.


#%% Exercise 10: Write a program to fetch only even values from a dictionary.


#%% Exercise 11: Define a function that accepts 2 values and returns its sum, subtraction, and multiplication.


#%% Exercise 12: Define a function that accepts roll numbers and returns whether the student is present or absent.


#%% Exercise 13: Define a function in python that accepts 3 values and returns the maximum of three numbers.


#%% Exercise 14: Define a function that accepts a number and returns whether the number is even or odd.


#%% Exercise 15: Define a function that counts vowels and consonants in a word.


#%% Exercise 16: Define a function that returns the Factorial of a number.


#%% Exercise 17: Define a function that accepts lowercase words and returns uppercase words.


#%% Exercise 18: Define a function that accepts radius and returns the area of a circle.


#%% Exercise 19: What is the difference between local and global variables?


#%% Exercise 20: What is the scope of a variable (in function)?


#%% Exercise 21: What is the difference between a parameter and an argument?


#%% Exercise 22: Name three iterable objects in Python.


#%% Exercise 23: What does a function return by default in Python?


#%% Exercise 24: Write a program to count vowels and consonants in a string.


#%% Exercise 25: Write a program to remove duplicates in a string.


#%% Exercise 26: Write a program to count the number of letters in a word.


#%% Exercise 27: Python program to count the occurrence of each character in a word.


#%% Exercise 28: Python program to convert lower letter to upper and upper letter to lower in a string.


#%% Exercise 29: Python program to search a specific word in a string.


#%% Exercise 30: Write a python program to sort letters of words by lower to upper case format.


#%% Exercise 31: Write a program in Python to count lower, upper, numeric, and special characters in a



#%% Exercise 32: Write a program in Python to remove an empty character from a list sequence.


#%% Exercise 33: Python program to convert all the starting letters of a word in upper case format or the title format.


#%% Exercise 34: Write a program to create a list with random data types elements.


#%% Exercise 35: Write a program to print all the elements of a list in a single line.


#%% Exercise 36: Write a program to count the number of items stored in a list.


#%% Exercise 37: Write a program to reverse a list in Python.


#%% Exercise 38: Python program to square each element of a list.


#%% Exercise 39: Python program to remove an empty element from a list.


#%% Exercise 40: Python program to append an element to a list.


#%% Exercise 41: Write a program to display those items from a list that is divisible by 5.


#%% Exercise 42: Write a program, to sum up, all the elements of a list.


#%% Exercise 43: Write a program to get the maximum number from a list


#%% Exercise 44: Write a program in Python to remove duplicate items from a list.


#%% Exercise 45: Write a program in Python to choose a random item from a list.


#%% Exercise 46: Write a program to append data from the second list to the first list.


#%% Exercise 47: Write a program in Python to filter odd and even number from a list.


#%% Exercise 48: Write a program to enter or append n numbers in a list.


#%% Exercise 49: Write a program in Python to remove repetitive items from a list.


#%% Exercise 50: Accept two numbers from the user and return their sum, multiplication, and division.


#%% Exercise 51: Write all the contents of a given file into a new file.


#%% Exercise 52: Read all the data from the text file except line number 5.


#%% Exercise 53: Accept three input values from the user in one input() call.


#%% Exercise 54: Accept input from the user and display the occurrence of that specific word from a text file.


#%% Exercise 55: Read a file and return the count of letters in a text file.


#%% Exercise 56: Read a file and return the count of words in a text file.


#%% Exercise 57: Read a file and check whether the word exists in a text file or not.


#%% Exercise 58: Write a program to Insert multiple data into a list.


#%% Exercise 59: Write a program to rename a text file in Python.


#%% Exercise 60: Write a program to check whether a given key exists in a dictionary or not.


#%% Exercise 61: Write a program to iterate over dictionary items using for loop.


#%% Exercise 62: Write a program to print only the keys of a dictionary.


#%% Exercise 63: Write a program to print the values of dictionary.


#%% Exercise 64: Write a program in python to map 2 lists into a dictionary.


#%% Exercise 65: Python program to remove a set of keys. Note: If we remove the key of the dictionary then the respective values of the dictionary should also be deleted. This means there are no values that exist without keys.


#%% Exercise 66: Python program to sort a dictionary by values (Ascending/ Descending).


#%% Exercise 67: Write a program to concatenate two dictionaries to create one.


#%% Exercise 68: Write a program, to sum up, all the values of a dictionary.


#%% Exercise 69: Write a program to get the maximum and minimum values of the dictionary.


#%% Exercise 70: Write a program to check if a dictionary is empty or not.


#%% Exercise 71: Write a program in Python to choose a random item from a list.


#%% Exercise 72: Write a program to sort dictionary values in python.


#%% Exercise 73: Write a program to check whether a key exists in the dictionary or not.


#%% Exercise 74: Write a program in python to map keys to the dictionary.


#%% Exercise 75: Write a program in Python to remove repetitive items from a list.











