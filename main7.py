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

#
def hello(name):
    print("Hello" , name)

hello("Devnath")
hello("Jayasekara")


#
def hello(name, age = 18):
    print("Hello", name, age)

hello("Devnath" , 20)
hello("Jayasekara", 22)
