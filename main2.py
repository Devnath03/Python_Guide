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
print(list1[3:6])  # Slicing from index 3 to 5
print(list1[6:])   # Slicing from index 6 to the end
print(list1[:3])   # Slicing from the start to index 2
print(list1[-3:])  # Slicing from the third last element to the end
print(list1[-6:-3])  # Slicing from the sixth last to the fourth last element
print(list1[-6:])  # Slicing from the sixth last element to the end

# Slicing with step
print(list1[::2])  # Slicing with a step of 2 (every second element)
print(list1[1::2])  # Slicing with a step of 2 starting from index 1 (every second element starting from the second element)
print(list1[::-1])  # Slicing the entire list in reverse order

# Slicing with negative step
print(list1[::-2])  # Slicing with a step of -2 (every second element in reverse order)

# Slicing with negative step starting from index -1
print(list1[-1::-2])  # Slicing with a step of -2 starting

#Membership Operators
print ('they are' in 'they are going to school')
print('they are' not in 'they are going to school')

#Checking membership in a list
num = [1, 2, 3, 4, 5]
print(1 in num)  # True, because 1 is in the list
print(6 in num)  # False, because 6 is not in the list  