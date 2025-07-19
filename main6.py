#
numbers = [ i + 2 for i in range(1 , 6)]
print(numbers)

number = [ i for i in range(1 , 11) if i % 2 == 0]
print (number)

# Initialize an empty list to store pairs
pairs = []

# Outer loop: i ranges from 1 to 3
for i in range(1, 4):
    # Inner loop: r ranges from 4 to 6
    for r in range(4, 7):
        # Append the pair (i, r) to the list
        pairs.append((i, r))

# Print the final list of pairs after both loops
print(pairs)

