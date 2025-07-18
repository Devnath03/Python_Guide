#Conditional Statements
# Conditional statements are used to perform different actions based on different conditions.
# They are used to execute a block of code only if a specified condition is true.
# Example of Conditional Statements
# If 10 is equal to 2, then print "This is true".
# In this case, the condition is false, so nothing will be printed.
if 10 == 2:
    print("This is true")

#Conditional statements for Day today Example
# If Today is Rainy Day We bring An Umbrella.
if "Rainy" == "Rainy":
    print("Bring an Umbrella")

# If Today is Sunny Day We bring Sunglasses.
if "Sunny" == "Sunny":  
    print("Bring Sunglasses")

# If Today is Snowy Day We bring a Jacket.
if "Snowy" == "Snowy":  
    print("Bring a Jacket")
    
#Conditional Statements with if-else
# Conditional statements can also include an else clause to execute a block of code when the condition is false.
if 10 == 2:
    print("This is true")
else:
    print("This is false")

#Conditional Statements with if-elif-else
# Conditional statements can also include multiple conditions using elif.
if 10 == 2:
    print("This is true")
elif 10 == 10:
    print("This is also true")
else:
    print("This is false")