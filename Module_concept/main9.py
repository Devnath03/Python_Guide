# Import the 'example' module which contains the custom 'add' function
import example

# Import the built-in 'math' module and give it an alias 'ma'
import math as ma

# Import only 'pi' from the math module and rename it as 'py'
from math import pi as py

# Call the 'add' function from the 'example' module with arguments 1 and 2
sum = example.add(1, 2)

# Print the result of the addition (should output 3)
print(sum)

# Print the value of pi using the math module alias
print(ma.pi)

# Print the square root of 81 using the math module alias
print(ma.sqrt(81))

