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

#del Method
# Using del to remove an element at a specific index
name = ['John', 'Doe', 'Smith', 'Jane']
del name[1:3]  # Removing the element at index 1 (which is 'Doe')
print(name)  # ['John', 'Smith', 'Jane']

#clear Method
# Using clear() to remove all elements from the list
name.clear()  # Removing all elements from the list
print(name)  # []


# This code snippet is intended to demonstrate the use of max() and min() functions with lists.
# However, it contains an error because max() and min() expect an iterable, not a list of lengths.
# To fix this, we should pass the lists directly to max() and min() instead of  
# passing a list of their lengths.
# Example of using max() and min() with lists
# The following code will raise an error
a = [ 1, 5 , 8]
b = [ 2, 6 ,9 , 10]
c = [ 100, 200]
print(max([len (a), len(b), len(c)]))  # This will raise an error because max() expects iterable, not a list of lengths
print(min([len(a), len(b), len(c)]))  # This will raise an error because min() expects iterable, not a list of lengths

# Correct usage of max() and min() with lists
print(max(3 , 4 , 2 ))
print(min(3 , 4 , 2 ))

# Joining elements of a list with different separators
names = ['John', 'Doe', 'Smith', 'Jane']
print("& ".join(sorted(names)))  # Joining sorted names with '&'

# Joining elements of a list with a comma
names = ['John', 'Doe', 'Smith', 'Jane']
names.append('Alice')  # Adding a new name to the list
print(", ".join(sorted(names)))  # Joining names with a comma

#Tuples
#Tuple Characteristics
# Tuples are ordered collections, meaning the order of elements is preserved.
# Tuples can contain elements of different data types, including integers, strings, and other tuples
# Tuples are immutable, meaning once created, their elements cannot be changed, added, or removed.
# Tuples can be nested, meaning a tuple can contain other tuples as elements.
# Example of a tuple with mixed data types
mixed_tuple = (1, 'apple', 3.14, (2, 4, 6))
print(mixed_tuple)  # Output: (1, 'apple', 3.14

# Tuples are immutable sequences in Python, meaning they cannot be changed after creation.
# Example of creating a tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)  # Output: (1, 2, 3, 4, 5)

# Accessing elements in a tuple 
print(my_tuple[0])  # Accessing the first element
print(my_tuple[1])  # Accessing the second element
print(my_tuple[2])  # Accessing the third element
print(my_tuple[3])  # Accessing the fourth element
print(my_tuple[4])  # Accessing the fifth element

# Accessing elements using negative indexing
print(my_tuple[-1])  # Accessing the last element
print(my_tuple[-2])  # Accessing the second last element
print(my_tuple[-3])  # Accessing the third last element

# Nested tuples
nested_tuple = ((1, 2), (3, 4), (5, 6))
print(nested_tuple)  # Output: ((1, 2), (3, 4), (5, 6))
# Accessing elements in the nested tuple
print(nested_tuple[0])  # Accessing the first sub-tuple 
print(nested_tuple[1])  # Accessing the second sub-tuple
print(nested_tuple[2])  # Accessing the third sub-tuple
print(nested_tuple[-1])  # Accessing the last sub-tuple
print(nested_tuple[-2])  # Accessing the second last sub-tuple  
print(nested_tuple[-3])  # Accessing the third last sub-tuple

# Accessing elements in the nested tuple
print(nested_tuple[0][0])  # Accessing the first element of the first   
print(nested_tuple[0][1])  # Accessing the second element of the first
print(nested_tuple[1][0])  # Accessing the first element of the second
print(nested_tuple[1][1])  # Accessing the second element of the second
print(nested_tuple[2][0])  # Accessing the first element of the third
print(nested_tuple[2][1])  # Accessing the second element of the third
print(nested_tuple[-1][-1])  # Accessing the last element of the last
print(nested_tuple[-2][-1])  # Accessing the last element of the second
print(nested_tuple[-3][-1])  # Accessing the last element of the third

# Slicing tuples
tuple1 = (1, 2, 3, 4, 5,    6, 7, 8, 9)
print(tuple1[0:3])  # Slicing from index 0 to 2
print(tuple1[3:6])  # Slicing from index 3 to 5
print(tuple1[6:])   # Slicing from index 6 to the end
print(tuple1[:3])   # Slicing from the start to index 2
print(tuple1[-3:])  # Slicing from the third last element to the end    
print(tuple1[-6:-3])  # Slicing from the sixth last to the fourth last element
print(tuple1[-6:])  # Slicing from the sixth last element to the end

#Combine Tuples
tuple2 = (10, 20, 30)
tuple3 = (40, 50, 60)
combined_tuple = tuple2 + tuple3  # Combining two tuples
print(combined_tuple)  # Output: (10, 20, 30, 40, 50, 60)

#Tuple Methods
# Count Method  
# The count() method returns the number of occurrences of a specified value in a tuple.
tuple4 = (1, 2, 3, 1, 4, 1)
print(tuple4.count(3))  # Output: 1, because 3 appears once in the tuple
print(tuple4.count(1))  # Output: 3, because 1 appears three times in the tuple

#Tuple Unpacking
# Tuple unpacking allows you to assign the elements of a tuple to multiple variables in a single
# line.
my_tuple = (1, 2, 3)
a, b, c = my_tuple  # Unpacking the tuple into variables a, b, and c
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3
print(a,b,c) # Output: 1 2 3

# Tuple unpacking with nested tuples
nested_tuple2 = ((1, 2), (3, 4), (5,6))
a, b, c = nested_tuple2  # Unpacking the nested tuple into variables a, b, and c
print(a)  # Output: (1, 2)
print(b)  # Output: (3, 4)
print(c)  # Output: (5, 6)
print(a[0], a[1])  # Output: 1 2
print(b[0], b[1])  # Output: 3 4
print(c[0], c[1])  # Output: 5 6

# Tuple unpacking with nested tuples and multiple variables
a, (b, c) = nested_tuple2[0], nested_tuple2[1]  # Unpacking the first element and the second element of the nested tuple
print(a)  # Output: (1, 2)

#Question 01 testing
fruits = ('apple', 'banana', 'cherry', 'date')
print(fruits[1])  # Output: 'banana'
print(len(fruits))  # Output: 4, because there are four elements in the tuple
print(fruits[2])  # Output: 'cherry', accessing the last element using negative indexing
print(fruits[1:4])  # Output: ('banana', 'cherry', 'date'), accessing the last element using negative indexing

# Question 02 testing
person = ('Alice', 30, 'Engineer')
a , b  , c = person  # Unpacking the tuple into variables a, b, and c
print(a)  # Output: 'Alice'
print(b)  # Output: 30
print(c)  # Output: 'Engineer'

# Question 03 testing
products = (
    ('Apple', 50, 1.2),
    ('Banana', 30, 0.5),
    ('Cherry', 100, 2.0),
    ('Date', 75, 1.5)
)
print(products[0][0]) # Output: 'Apple', accessing the first product's name
print(products[1][1]) # Output: 30, accessing the second product's quantity
print(products[2][2]) # Output: 2.0, accessing the third product's price
print(products[3][0]) # Output: 'Date', accessing the fourth product's name
print(products[0][1:3]) # Output: (50, 1.2), accessing the first product's quantity and price


