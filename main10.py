# Define a class named 'animal'
class animal:
    # Class-level attributes (shared across all instances unless overridden)
    name = ''
    age = 0
    color = ''

    # Method to simulate the animal eating food
    def eat(self, food):
        print(food, 'eat')

# Create an instance of the 'animal' class
cat = animal()

# Set the name attribute of the cat instance to 'cat'
cat.name = 'cat'

# Print the name of the cat
print("Method is" , cat.name)

# Call the 'eat' method on the cat instance with 'fish' as an argument
cat.eat('fish')


# Here's your Python code with explanatory for clarity, especially around inheritance:
# Base class named 'Animal'
class Animal:
    # Class attribute 'name' (shared unless set in an instance)
    name = ''

    # Method that prints a generic eating behavior
    def eat(self):
        print('eat')

# Derived class 'dog' that inherits from the base class 'Animal'
class dog(Animal):
    # Additional method specific to the 'dog' class
    def test(self):
        print("I am a Dog")

# Create an instance of the 'dog' class
animal1 = dog()

# Call the inherited 'eat' method from the 'Animal' class
animal1.eat()

# Set the 'name' attribute for the 'animal1' instance
animal1.name = 'Zeeyara'

# Print the name of the dog
print(animal1.name)


# Encapsulation Example 1: Using private variables and getters/setters
class Student:
    # Private attribute (name is made private by using double underscores)
    __name = ''

    # Getter method to access the private attribute
    def getname(self):
        return self.__name

    # Setter method to modify the private attribute
    def setname(self, name):
        self.__name = name

# Create an instance of Student
ob1 = Student()

# Set the private name attribute using the setter method
ob1.setname('Jhon')

# Access and print the name using the getter method
print(ob1.getname())
print()


# Encapsulation Example 2: Using constructor (__init__) for attribute initialization
class animal:
    # Constructor method with parameters for name and age
    def __init__(self, Name, age):
        # Public attributes (no underscore, accessible outside)
        self.name = Name
        self.age = age

# Create an instance of the animal class
ob1 = animal('dog', 10)

# Access and print the public attributes
print(ob1.name)
print(ob1.age)
