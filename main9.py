# Try to execute the code that might raise an exception
try:
    # Attempt to divide 7 by 0 (this wl cause a ZeroDivisionError)
    print(7 / 0)

# If a ZeroDivisionError occurs, this block wl execute
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
finally:
    print("Other Error occured")

# This line runs after the try-except block
print("This is the end of the program.")

print ()

# Try to execute the file reading operation
try:
    # Attempt to open a file named 'data.txt' in read mode ('r')
    fe = open("data.txt", "r")

    # Try to read the content of the file
    # (Note: there's a typo in 'read' — it's written as 'raed')
    content = fe.raed()  # <-- This will cause an AttributeError due to the typo

    # Print the content of the file
    print(content)

    # Close the file after reading
    fe.close()

# This block executes if the file is not found
except FileNotFoundError:
    print("File Not Found")

# This block always executes whether or not an exception occurs
finally:
    print("Execution Completed")

# This line runs after everything else
print("End of Program")
