#Sets
#Sets in Python are unordered collections of unique elements.
#Creating a Set
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

#Dictionaries
#Dictionary in Python is a collection of key-value pairs.
#Creating a Dictionary
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York , USA , Canada , UK"
}
print(my_dict)

#Accessing Dictionary Values
print(my_dict["name"])  # Accessing value by key
print(my_dict["age"])
print(my_dict["city"])

#Adding Key-Value Pairs to a Dictionary
my_dict["email"] = "alice@example.com"
print(my_dict)  

#Removing Key-Value Pairs from a Dictionary
del my_dict["age"]  
print(my_dict)

#Clearing a Dictionary
my_dict.clear()
print(my_dict)

#Pop a Dictionary
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
popped_value = my_dict.pop("age")
print("Popped Value:", popped_value)
print("Dictionary after pop:", my_dict)
#Add Variable In the String type command line using f string
f"Current Dictionary: {my_dict}"

#Compound Data Structures
#Compound Data Structures are data structures that can hold multiple values and can be nested within each other.
#Creating a Compound Data Structure
my_compound_structure = {
    "name": "Alice",
    "age": 30,
    #List Type Elemts
    "hobbies": ["reading", "traveling", "swimming"],
    "address": {
        #Dictionary Type Elements
        "street": "123 Main St",
        "city": "New York",
        "country": "USA"
    },
    'anupam': {
        'age': 25,
        'Degree': 'B.Tech',
        'Marks': [85.5, 80, 90.0]
    },
}
print("Compound Data Structure:", my_compound_structure)

#Accessing Elements in Compound Data Structures
print("Name:", my_compound_structure["name"])
print("Age:", my_compound_structure["age"])
print("Hobbies:", my_compound_structure["hobbies"])
print("Address:", my_compound_structure["address"])
print("Street:", my_compound_structure["address"]["street"])
print("City:", my_compound_structure["address"]["city"])    
print("Country:", my_compound_structure["address"]["country"])

#Adding Elements to Compound Data Structures
my_compound_structure["email"] = "alice@example.com"    
print("After Adding Email:", my_compound_structure)

#Removing Elements from Compound Data Structures
del my_compound_structure["age"]
print("After Removing Age:", my_compound_structure)

#Clearing Compound Data Structures
my_compound_structure.clear()
print("After Clearing:", my_compound_structure)

#Pop a Compound Data Structure
my_compound_structure = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
popped_value = my_compound_structure.pop("age")
print("Popped Value:", popped_value)
print("Dictionary after pop:", my_compound_structure)   

#Add Variable In the String type command line using f string
f"Current Compound Data Structure: {my_compound_structure}"

#Add Spaces in print command
print ()
print ()

#Add mark to the Anupam
#Test Only Command Line, After run show error because of empty list happens via the pop command & Removing commands
my_compound_structure['anupam']['Marks'].append(100)
print("After Adding Marks to Anupam:", my_compound_structure)

