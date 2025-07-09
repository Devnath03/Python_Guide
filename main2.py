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

#Mutable and Immutable Types
# Mutable types can be changed after creation, while immutable types cannot.
# Example of a mutable type (list)
fruit = ['apple', 'banana', 'cherry']
fruit[0] = 'kiwi'  # Changing the first element
print(fruit)  # ['kiwi', 'banana', 'cherry']

# Example of an immutable type (string)
name = 'John'
name2 = name
name = 'Doe'  # Changing name does not affect name2
print(name)  # 'Doe', name is now 'Doe'
print(name2)  # 'John', name2 remains unchanged

# Example of mutable types (list)
num = [1,2,3,4,5,6,7,8,9,10]
num2 = num
num[0] = 100  # Changing the first element of num
print(num)  # [100, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(num2)  # [100, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(num is num2)  # True, both variables point to the same list object

#Joint Methods
name = ['John', 'Doe' ,'Smith', 'Jane']
# Joining elements of a list into a string
full_name = '\n '.join(name)
print(full_name)  # 'John\n Doe\n Smith\n Jane'
# Joining elements of a list with a comma
full_name_with_comma = ', '.join(name)
print(full_name_with_comma)  # 'John, Doe, Smith, Jane'
# Joining elements of a list with a space
full_name_with_space = ' '.join(name)
print(full_name_with_space)  # 'John Doe Smith Jane'
# Joining elements of a list with a hyphen
full_name_with_hyphen = '-'.join(name)
print(full_name_with_hyphen)  # 'John-Doe-Smith-Jane'
# Joining elements of a list with a custom separator
full_name_with_custom = ' | '.join(name)
print(full_name_with_custom)  # 'John | Doe | Smith | Jane'
# Joining elements of a list with a newline character
full_name_with_newline = '\n'.join(name)
print(full_name_with_newline)  # 'John\nDoe\nSmith\nJane'

# Adding a new name to the list
name.append('Alice')  # Adding a new name to the list
full_name_after_append = '\n '.join(name)
print(full_name_after_append)  # 'John\n Doe\n Smith\n Jane\n Alice'

#Inserting a new name at a specific position
name.insert(2, 'Bob')  # Inserting 'Bob' at index 2
full_name_after_insert = '\ '.join(name)
print(full_name_after_insert)  # 'John\ Bob\ Smith\ Jane\ Alice'

# Removing a name from the list
name.remove('Doe')  # Removing 'Doe' from the list
full_name_after_remove = '6 '.join(name)
print(full_name_after_remove)  # 'John\ Bob\ Smith\ Jane\ Alice'

# Sorting the list of names
name.sort()  # Sorting the list in alphabetical order
full_name_after_sort = '\ '.join(name)
print(full_name_after_sort)  # 'Alice\ Bob\ John\ Smith\ Jane'

# Reversing the list of names
name.reverse()  # Reversing the order of the list
full_name_after_reverse = '\ '.join(name)
print(full_name_after_reverse)  # 'Jane\ Smith\ Bob\ John\ Alice'

#Pop Method
# Using pop() to remove and return the last element
removed_name = name.pop(2)  # Removes 'Alice'
print(removed_name)  # 'Alice'
full_name_after_pop = '\ '.join(name)
print(full_name_after_pop)  # 'Jane\ Smith\ Bob\ John'

#Remove Indexes
name = ['John', 'Doe', 'Smith', 'Jane']
del name[1:3]  # Removing the element at index 1 (which is 'Doe')
print(name)  # ['John', 'Smith', 'Jane']


