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
print(cat.name)

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
