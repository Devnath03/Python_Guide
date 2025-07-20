# Try to execute the code that might raise an exception
try:
    # Attempt to divide 7 by 0 (this will cause a ZeroDivisionError)
    print(7 / 0)

# If a ZeroDivisionError occurs, this block will execute
except ZeroDivisionError:
    print("A ZeroDivisionError occurred")

# Catch any other type of error
except:
    print("An error occurred")

# This line runs after the try-except block, no matter what
print("This is the end of the program.")


# Second Example with multiple print statements that can raise exceptions
try:
    # Attempt to divide 7 by 0 multiple times (each line would raise ZeroDivisionError)
    print(7 / 0)
    print(7 / 0)
    print(7 / 0)
    print(7 / 0)

# Specific exception should come first
except ZeroDivisionError:
    print("A ZeroDivisionError occurred")

# Then you can add other specific exceptions like this (though IndentationError won't be caught at runtime)
except IndentationError:
    print("An IndentationError occurred")

# General fallback for any other type of exception
except:
    print("An error occurred")

# This line runs after the try-except block
print("This is the end of the program.")
