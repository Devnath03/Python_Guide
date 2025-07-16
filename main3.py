#Sets
my_set = {1, 2, 3, 4, 5}
print(my_set)

#Sets Duplication
my_set_with_duplicates = {1, 2, 2, 3, 4, 5 ,6 , 5}
print(my_set_with_duplicates)  # Duplicates are removed in sets

#Types of Sets
empty_set = set()  # Empty set
print(empty_set)
# Non-empty set
non_empty_set = {1, 2, 3}  # Non-empty set
print(non_empty_set)
# Set with mixed data types
mixed_set = {1, "Hello", 3.14, (1, 2)}
print(mixed_set)

#Adding Elements to a Set
my_set1 = {1, 2, 3}
my_set1.add(6)
print(my_set1)

#Removing Elements from a Set
my_set1.remove(2)
print(my_set1)

#Clear a Set
my_set1.clear()
print(my_set1)

#Pop a Set
my_set1 = {1, 2, 3}
popped_element = my_set1.pop()
print(popped_element)
print(my_set1)

#Sample Question 01 to test Sets
# Creating a Sample_set
Sample_set = {101, 102, 103, 104, 105}
print("Sample Set :", Sample_set)
# Adding an element to the Sample_set
Sample_set.add(106)
print("Added New Set :", Sample_set)
# Removing an element from the Sample_set
Sample_set.remove(102)
Sample_Pop = Sample_set.pop()
print("Popped Element :", Sample_Pop)
print("Final Sample Set :", Sample_set)
#Clearing the Sample_set
Sample_set.clear()
print("Cleared Sample Set :", Sample_set)
