# ---------------------------------------------
# List Comprehensions and Nested Loops Examples
# ---------------------------------------------

# Create a list by adding 2 to each number from 1 to 5
# [1+2, 2+2, 3+2, 4+2, 5+2] => [3, 4, 5, 6, 7]
numbers = [i + 2 for i in range(1, 6)]
print(numbers)

# Create a list of even numbers from 1 to 10 using a condition inside the list comprehension
# Keeps only numbers divisible by 2
number = [i for i in range(1, 11) if i % 2 == 0]
print(number)

# ---------------------------------------------
# Nested Loops (Without List Comprehension)
# ---------------------------------------------

# Initialize an empty list to store pairs
lists = []

# Outer loop: i takes values from 1 to 3
for i in range(1, 4):
    # Inner loop: r takes values from 4 to 6
    for r in range(4, 7):
        # Add the tuple (i, r) to the list
        lists.append((i, r))

# Output: All combinations of i (1 to 3) with r (4 to 6)
print(lists)

# ---------------------------------------------
# Same Nested Loop using List Comprehension
# ---------------------------------------------

# Creates list of tuples (p, j) using nested loops
# p ranges from 1 to 3, j ranges from 4 to 6
list = [(p, j) for p in range(1, 4) for j in range(4, 7)]
print(list)

# ---------------------------------------------
# Flattening a Matrix (Using Loops)
# ---------------------------------------------

# Define a 2D list (matrix)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Create an empty list to store the flattened elements
flattend = []

# Outer loop iterates through each row of the matrix
for row in matrix:
    # Inner loop iterates through each number in the row
    for num in row:
        flattend.append(num)  # Add number to the flat list

# Output: Flattened list of all elements
print(flattend)
print()

# ---------------------------------------------
# Flattening a Matrix (Using List Comprehension)
# ---------------------------------------------

# More compact way to flatten the matrix in one line
# For each row in matrix, for each number in row, include in the list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattends = [num for row in matrix for num in row]
print(flattends)

# ---------------------------------------------
# Replace Negative Numbers with 0 (List Comprehension)
# ---------------------------------------------

# Original list containing both negative and positive numbers
numbers = [-5, 3, -1, 7, -2]

# Create a new list where:
# - If the number is non-negative (>= 0), keep it as is
# - If the number is negative (< 0), replace it with 0
non_negative = [x if x >= 0 else 0 for x in numbers]
print(non_negative)  # Output: [0, 3, 0, 7, 0]

# ---------------------------------------------
# Another Example: Replace Negatives with 0
# ---------------------------------------------

# Another list with mixed numbers
num_list = [-7, 8, 6, 5, -3, 4]

# Same logic: keep numbers >= 0, replace others with 0
renegative = [x if x >= 0 else 0 for x in num_list]
print(renegative)  # Output: [0, 8, 6, 5, 0, 4]

# ---------------------------------------------
# Repetition of the same operation on the same list
# ---------------------------------------------

# Same input and same transformation
num_list = [-7, 8, 6, 5, -3, 4]
renegative = [x if x >= 0 else 0 for x in num_list]
print(renegative)  # Output: [0, 8, 6, 5, 0, 4]
print()

# --------------------------------------
# List Comprehension with zip()
# --------------------------------------

# Define two lists of equal length
list = [1, 2, 3]
list1 = [4, 5, 6]

# Use zip() to pair elements from both lists and add corresponding elements
# This creates a new list with the sum of elements at each position
sum_list = [x + y for x, y in zip(list, list1)]

# Output: [5, 7, 9]
print(sum_list)

# --------------------------------------
# Transposing a Matrix
# --------------------------------------

# Define a 3x3 matrix (nested list)
matrix = [
    [1, 2, 3],   # Row 0
    [4, 5, 6],   # Row 1
    [7, 8, 9],   # Row 2
]

# Transpose the matrix using nested list comprehension
# For each column index (i), extract the i-th element from every row
transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

# Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
print(transpose)
print()

#
dataster = [
    [1, 200, None ],
    [2, 300, 2.5],
    [3, 400, 0.7],
    [4, 500, None],
]

output = [ col for col in dataster if col[2] is not None]
print(output)

data = [
    [1, 200, None ],
    [2, 300, 0.5],
    [3, None, 0.7],
    [None, 500, 0.2],
]

outs = [ row for row in data ] 
print(outs)
print()
out = [ row for row in data ]
print(out)