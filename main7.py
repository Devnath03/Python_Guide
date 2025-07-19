# ---------------------------------------
# Functions
# ---------------------------------------

# Functions are reusable blocks of code that perform a specific task.
# They help make programs more organized, readable, and modular.

# ---------------------------------------
# Functions Mean
# ---------------------------------------

# A function can take input (called parameters), process it, and return output (called return value).
# Python provides built-in functions (like print(), len(), sum()) and also allows user-defined functions.
# Example of built-in function: sum([1, 2, 3])  -> returns 6

# ---------------------------------------
# Defining Functions
# ---------------------------------------

# In Python, functions are defined using the 'def' keyword.
# Syntax:
# def function_name(parameters):
#     # function body
#     return result

# ---------------------------------------
# Single Parameter
# ---------------------------------------

# Define a function named 'hello' that takes one parameter: 'name'
def hello(name):
    # Print a greeting message with the given name
    print("Hello", name)

# Call the function with the argument "Devnath"
hello("Devnath")  # Output: Hello Devnath

# Call the function with the argument "Jayasekara"
hello("Jayasekara")  # Output: Hello Jayasekara


# ---------------------------------------
# Default Parameter Value
# ---------------------------------------

# Define a function 'hello' with two parameters: 'name' and 'age'
# 'age' has a default value of 18, so it is optional when calling the function
def hello(name, age = 18):
    # Print a greeting message including name and age
    print("Hello", name, age)

# Call the function with both name and age provided
hello("Devnath", 20)  # Output: Hello Devnath 20

# Call the function with both name and age provided
hello("Jayasekara", 22)  # Output: Hello Jayasekara 22
print()

# ---------------------------------------
# Function with Default Argument and Return Value
# ---------------------------------------

# Define a function that takes a name and age (default is 15 if not provided)
def hello(name, age=15):
    # Returns a greeting string, age is converted to string for concatenation
    return "Hello " + name + " " + str(age)

# Call the function and store the returned value in variables
it = hello("Devnath", 22)
its = hello("Jayasekara", 25)

# Print the returned greeting messages
print(it)   # Output: Hello Devnath 22
print(its)  # Output: Hello Jayasekara 25


# ---------------------------------------
# Variable Scope Example
# ---------------------------------------

# Global variable (accessible everywhere)
message = "Hello World"

# Define a function to modify the global variable
def test():
    global message  # Tells Python to use the global variable
    message = "Hello World now"  # Modify the global variable
    print(message)  # Output: Hello World now

# Call the function
test()


# ---------------------------------------
# Function with Docstring (Documentation)
# ---------------------------------------

# Define a function to add two numbers, with a proper docstring
def add(a, b):
    a = 20
    b = 12
    """
    This function adds two numbers.

    Parameters:
        a (int): First number
        b (int): Second number

    Returns:
        int: Sum of a and b
    """
    return a + b

# Example usage
print(add(5, 3))  # Output: 8


# ---------------------------------------
# Sample Question
# 1. Basic Function Example
# ---------------------------------------

# Define a function that accepts a user's name and a book title
def library(name, title):
    # Returns a formatted message saying the user borrowed the book
    return " " + name + " Borrowed " + title + " From the Library."

# Call the function with name and book title, and store the result
book = library("Jhon", "The Great Gatsby")

# Print the result
print(book)  # Output:  Jhon Borrowed The Great Gatsby From the Library.
print()      # Prints a blank line for spacing


# ---------------------------------------
# 2. Function with History Tracking
# ---------------------------------------

# Create an empty list to store borrowing history
history = []

# Define a function that also logs the borrowing action into the 'history' list
def library(name, title):
    # Append a dictionary with name and title to the history list
    history.append({"name": name, "title": title})
    
    # Return a formatted borrowing message
    return " " + name + " Borrowed " + title + " From the Library."

# Call the function, which adds to history and returns the message
book = library("Jhon", "The Great Gatsby")

# Print the borrowing message
print(book)  # Output:  Jhon Borrowed The Great Gatsby From the Library.

# ---------------------------------------
# Lambda Expressions
# ---------------------------------------

# Lambda expression for addition
# 'lambda x, y: x + y' defines an anonymous function that returns the sum of x and y
add = lambda x, y: x + y
print(add(2, 3))  # Output: 5


# ---------------------------------------
# Using lambda with filter() function
# ---------------------------------------

# Define a set of city names
cities = { "New York", "Canada", "United Kingdom", "Chicago", "Mount View", "Denver" }

# Use filter() to select only cities with name length less than 10 characters
# lambda city: len(city) < 10 is the filtering condition
short_cities = list(filter(lambda city: len(city) < 10, cities))

# Print the filtered list of short-named cities
print(short_cities)  # Output may vary based on set order


# ---------------------------------------
# Repeated Lambda Usage for Different Operations
# ---------------------------------------

# Lambda for addition again (redefined as 'adds')
adds = lambda p, q: p + q
print(adds(20, 30))  # Output: 50
print(adds(12, 13))  # Output: 25
print(adds(21, 31))  # Output: 52


# Lambda for multiplication (reusing same variable name 'adds')
adds = lambda p, q: p * q
print(adds(20, 30))  # Output: 600
print(adds(12, 13))  # Output: 156
print(adds(21, 31))  # Output: 651


# Lambda for subtraction (again reusing 'adds')
adds = lambda p, q: p - q
print(adds(20, 30))  # Output: -10
print(adds(12, 13))  # Output: -1
print(adds(21, 31))  # Output: -10



