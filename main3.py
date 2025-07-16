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
