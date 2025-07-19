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
