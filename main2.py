# Create List
fruits = [' apple', 'banana', 'grapes']
print(fruits)

# Accessing elements in the list
print(fruits[0])  # Accessing the first element
print(fruits[1])  # Accessing the second element
print(fruits[2])  # Accessing the third element

# Accessing elements using negative indexing
print(fruits[-1])  # Accessing the last element
print(fruits[-2])  # Accessing the second last element
print(fruits[-3])  # Accessing the third last element

#Nested List
nested_list = [['apple', 'banana'], ['grapes', 'orange'], ['kiwi', 'mango']]
print(nested_list)

# Accessing elements in the nested list
print(nested_list[0])  # Accessing the first sub-list
print(nested_list[1])  # Accessing the second sub-list
print(nested_list[2])  # Accessing the third sub-list

# Accessing elements using negative indexing
print(nested_list[-1])  # Accessing the last sub-list
print(nested_list[-2])  # Accessing the second last sub-list
print(nested_list[-3])  # Accessing the third last sub-list

# Accessing elements in the nested list
print(nested_list[0][0])  # Accessing the first element of the first
print(nested_list[0][1])  # Accessing the second element of the first
print(nested_list[1][0])  # Accessing the first element of the second
print(nested_list[1][1])  # Accessing the second element of the second
print(nested_list[2][0])  # Accessing the first element of the third    
print(nested_list[2][1])  # Accessing the second element of the third
print(nested_list[-1][-1])  # Accessing the last element of the last sub-list
print(nested_list[-2][-1])  # Accessing the last element of the second

#Slice List
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list1[0:3])  # Slicing from index 0 to 2