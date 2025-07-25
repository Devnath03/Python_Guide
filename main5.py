# While loop
# A while loop is a control structure in Python that repeats a block of code as long as a condition is true.
# Example 1: Print "Hello" five times using a while loop
x = 1
while (x <= 5):
    print("Hello")   # prints "Hello"
    x = x + 1        # increment x by 1 after each iteration

# Example 2: Print numbers from 1 to 10
initial = 1
while initial <= 10:
    print(initial)   # prints the current value of 'initial'
    initial += 1     # increment 'initial' by 1

# Example 3: Calculate the sum of the first 'n' positive integers
n = int(input("Enter a Integer no Here : "))  # take user input and convert to integer

sum = 0   # initialize sum to 0
i = 1     # initialize counter to 1
while i <= n:
    sum = sum + i   # add current value of i to sum
    i = i + 1       # increment i by 1
print("The sum of the first", n, "positive integers is:", sum)

# Example 4: Password check using while loop
correct_password = "1234"                     # predefined correct password
password = input("Enter your password : ")    # prompt user to enter password
while password != "1234":                     # loop runs as long as password is incorrect
    print("Incorrect Password")               # notify user
    password = input("Enter your password : ")# ask again
print("Password Correct")                     # printed after correct password is entered

# ---------------------------------------------------------------
#           For Loops & While Loops — Key Differences
# ---------------------------------------------------------------
# | Feature       | For Loop                                  | While Loop                                  |
# |---------------|-------------------------------------------|---------------------------------------------|
# | Purpose       | Used when the number of iterations        | Used when the number of iterations          |
# |               | is known.                                 | is unknown.                                 |
# |---------------|-------------------------------------------|---------------------------------------------|
# | Syntax        | for item in sequence:                     | while condition:                            |
# |               |     # Code                                |     # Code                                  |
# |---------------|-------------------------------------------|---------------------------------------------|
# | Control       | Iterates over a sequence (range, list,    | Continues as long as the condition is True  |
# |               | etc.)                                     |                                             |
# |---------------|-------------------------------------------|---------------------------------------------|
# | Termination   | Ends when the sequence is exhausted.      | Ends when the condition becomes False.      |
# |---------------|-------------------------------------------|---------------------------------------------|
# | Example       | for i in range(5):                        | count = 0                                   |
# |               |     print(i)                              | while count < 5:                            |
# |               |                                           |     print(count)                            |
# |---------------|-------------------------------------------|---------------------------------------------|
# | When to Use   | When you know how many times to loop.     |When you don’t know the number of iterations.|
# ----------------------------------------------------------------------------------------------------------

# -------------------------------
# Break Statement Example
# -------------------------------
# The 'break' statement is used to exit the loop completely
# when a specific condition is met.

print("Break Statement Output:")
for i in range(5):  # Loop from 0 to 4
    if i == 2:       # When i equals 2
        break        # Exit the loop immediately
    print(i)         # Print the value of i (only if i < 2)

# Output will be:
# 0
# 1


# -------------------------------
# Continue Statement Example
# -------------------------------
# The 'continue' statement is used to skip the current iteration
# and move to the next one.

print("\nContinue Statement Output:")
for i in range(5):  # Loop from 0 to 4
    if i == 2:       # When i equals 2
        continue     # Skip the rest of the code in this iteration
    print(i)         # Print the value of i (except when i == 2)

# Output will be:
# 0
# 1
# 3
# 4


# ---------------------------------------------------------------
#                   Break vs. Continue in Loops
# ----------------------------------------------------------------------------------------------------------|
# | Feature      | Break                                      | Continue                                    |
# |--------------|--------------------------------------------|---------------------------------------------|
# | Purpose      | Exits the loop entirely.                   | Skips the current iteration and continues.  |
# |--------------|--------------------------------------------|---------------------------------------------|
# | When to Use  | When you want to stop looping              | When you want to skip an iteration and      |
# |              | based on a condition.                      | continue.                                   |
# |--------------|--------------------------------------------|---------------------------------------------|
# | Example      | Stop when a certain condition is met.      | Skip an iteration when a condition is met.  |
# |--------------|--------------------------------------------|---------------------------------------------|
# | Loop Type    | Works in both for and while loops.         | Works in both for and while loops.          |
# ----------------------------------------------------------------------------------------------------------|

# ---------------------------------------------------
#                  Zip and Enumerate
# ---------------------------------------------------

# -----------------------
# zip()
# -----------------------
# The zip() function takes two or more sequences (like lists or tuples)
# and combines them into pairs (or tuples) by matching elements of the same position.
# For example, the first element of each sequence forms the first pair, 
# the second elements form the second pair, and so on.
# If the sequences are not the same length, zip() stops when the shortest sequence ends.
#
# This is useful when you want to iterate over multiple sequences in parallel.

# Example usage of zip():
print(list(zip([1, 2, 3], [7, 8, 9])))
# Output: [(1, 7), (2, 8), (3, 9)]
# Explanation: The first elements (1 and 7) are paired,
# second elements (2 and 8), third elements (3 and 9).

# Now, suppose you have a list of pairs and want to unzip them back into separate lists:
list_of_pairs = [(1, 7), (2, 8), (3, 9)]

# The * operator unpacks the list_of_pairs into separate arguments for zip()
x, y = zip(*list_of_pairs)

print(x)  # Output: (1, 2, 3)
print(y)  # Output: (7, 8, 9)
# Explanation: zip(*list_of_pairs) "unzips" the pairs into separate tuples.

# -----------------------
# enumerate()
# -----------------------
# The enumerate() function adds a counter/index to an iterable,
# returning pairs of (index, value) for each item.
# It helps when you need to keep track of the position of elements while looping,
# without manually incrementing a counter variable.

# Create a list of letters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# Use enumerate() to loop through the list with both index and value
for i, letter in enumerate(letters):
    # i is the index (position) of the current letter
    # letter is the actual character from the list

    # Print the index of the current element
    print("Index :", i)
    # Print the corresponding letter at that index
    print("Letter is :", letter)

# ----------------------------
# List Comprehensions Examples
# ----------------------------

# Creating a list by copying all elements from another list
fruits = ["apple", "Banana" , "Cherry"]
full_fruits = [fruit for fruit in fruits]  # Copies each element from the fruits list
print(full_fruits)  # Output: ['apple', 'Banana', 'Cherry']

# Creating a list of fruits in uppercase, excluding "Banana"
fruits = ["apple", "Banana" , "Cherry"]
filtered_fruits = [fruit.upper() for fruit in fruits if fruit != "Banana"]
# fruit.upper() --> Converts fruit name to uppercase
# if fruit != "Banana" --> Filters out "Banana"
print(filtered_fruits)  # Output: ['APPLE', 'CHERRY']

# Creating a list with only "Banana" in uppercase
fruits = ["apple", "Banana" , "Cherry"]
filtered_fruits = [fruit.upper() for fruit in fruits if fruit == "Banana"]
# if fruit == "Banana" --> Includes only "Banana"
print(filtered_fruits)  # Output: ['BANANA']

# Adding a suffix "Fru" to each fruit name in uppercase
fruits = ["apple", "Banana" , "Cherry"]
filtered_fruits = [fruit.upper() + "Fru" for fruit in fruits]
# fruit.upper() + "Fru" --> Converts to uppercase and adds "Fru"
print(filtered_fruits)  # Output: ['APPLEFru', 'BANANAFru', 'CHERRYFru']
print()

# ----------------------------
# List Comprehensions on Nested Lists
# ----------------------------

# Nested list: each inner list contains [id, value, ratio]
data = [
    [1, 200, None],
    [2, 300, 0.5],
    [3, 250, 0.7],
    [4, 500, 0.5]
]

# Extract the first column (IDs) if it's not None
column_values = [row[0] for row in data if row[0] is not None]
# row[0] --> Gets the ID from each row
# if row[0] is not None --> Ensures ID exists
print(column_values)  # Output: [1, 2, 3, 4]
print()

# Extract the second column (values) if it's not None
column_values = [row[1] for row in data if row[1] is not None]
# row[1] --> Gets the value from each row
print(column_values)  # Output: [200, 300, 250, 500]
print()

# Extract the third column (ratios) only if the second column is not None
column_values = [row[2] for row in data if row[1] is not None]
# row[2] --> Gets the ratio
# if row[1] is not None --> Ensures the value column is present
print(column_values)  # Output: [None, 0.5, 0.7, 0.5]
print()
