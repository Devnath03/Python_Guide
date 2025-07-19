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

# 
def hello(name,age=15):
    return "Hello"+ "" + name + " " + str(age)

it = hello("Devnath" , 22)
its = hello("jayasekara" , 25)
print(it)
print(its) 

#variable Scpopre
# Global scope
message = "Hello World"

def test ():
    global message 
    message = "Hello World now"
    print(message)

test()
