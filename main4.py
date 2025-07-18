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

#Conditional Statements with Nested if
# Conditional statements can be nested within each other to check multiple conditions.
if 10 == 10:
    print("Outer condition is true")
    if 5 == 5:
        print("Inner condition is also true")   
# Conditional statements can also be used to check for multiple conditions using logical operators.
if 10 == 10 and 5 == 5:
    print("Both conditions are true")
else:
    print("At least one condition is false")
# Conditional statements can also be used to check for multiple conditions using logical operators.
if 10 == 10 or 5 == 6:  
    print("At least one condition is true")
# Conditional statements can also be used to check for multiple conditions using logical operators.
if not (10 == 2):
    print("The condition is false, so this will be printed")
# Conditional statements can also be used to check for multiple conditions using logical operators.
if 10 != 2:
    print("10 is not equal to 2, so this will be printed")
# Conditional statements can also be used to check for multiple conditions using logical operators.
if 10 < 20:
    print("10 is less than 20, so this will be printed")
# Conditional statements can also be used to check for multiple conditions using logical operators.
if 20 > 10:
    print("20 is greater than 10, so this will be printed")

#sample Questions
# # 1. The person must have a credit score of 700 or higher.
# credit_score = 750  # Example value; you can change this as needed
# if credit_score >= 700:
#     print("The person is eligible for the loan.")
# else:
#     print("The person is not eligible for the loan.")

# print()

# # 2. The person must have annual income of $50,000 or more.
# annual_income = 50000  # Example value; you can change this as needed
# if annual_income >= 50000:
#     print("The person is eligible for the loan.")
# else:
#     print("The person is not eligible for the loan.")

# # 3. If the person self-employed, their income requirements is reduced to $40,000 or more.
# self_employed = True  # Example value; you can change this as needed
# if self_employed:
#     if annual_income >= 40000:
#         print("The self-employed person is eligible for the loan.")
#     else:
#         print("The self-employed person is not eligible for the loan.")

# # 4. The Person doesn'tmeet this criteria, they are not eligible for the loan.
# if not (credit_score >= 700 or annual_income >= 50000 or (self_employed and annual_income >= 40000)):
#     print("The person is not eligible for the loan.")

credit_score = 750
annual_income = 50000
self_employed = False

if credit_score >= 700:
    if self_employed :
        if annual_income >=40000:
            print("You Qualified for loan")
        else:
            print("You don't qualify for loan")
    else:
        if annual_income >= 45000:
            print("You Qualify for loan")
        else:
            print("You don't qualify the loan")
else:
    print("You  don't qualify for loan.")


# -------------------------------
# BOOLEAN EXPRESSIONS (Loan Check)
# -------------------------------

# Case where outer condition is True (will always execute this block)
if True:
    if self_employed:  # Check if the user is self-employed
        if annual_income >= 40000:
            print("You Qualified for loan")  # Self-employed income requirement: 40,000+
        else:
            print("You don't qualify for loan")
    else:  # If not self-employed
        if annual_income >= 45000:
            print("You Qualify for loan")  # Regular income requirement: 45,000+
        else:
            print("You don't qualify the loan")
else:
    print("You  don't qualify for loan.")  # This won't run

# Case where outer condition is False (skips entire block and runs only else)
if False:
    if self_employed:
        if annual_income >= 40000:
            print("You Qualified for loan")
        else:
            print("You don't qualify for loan")
    else:
        if annual_income >= 45000:
            print("You Qualify for loan")
        else:
            print("You don't qualify the loan")
else:
    print("You  don't qualify for loan.")  # This will always run in this case

# -------------------------------
# FOR LOOPS (Iterating Cities and Ranges)
# -------------------------------

# A set of cities
cities = {'Canada', 'New York', 'Chicago', 'America'}

# Looping through the set and printing each city in upper and lower case
for city in cities:
    print(city.upper())  # Convert city name to uppercase
    print(city.lower())  # Convert city name to lowercase
print("Done")  # End of city loop

# Print "Hello" 20 times
for i in range(20):
    print("Hello")

# Print numbers from 5 to 9
for i in range(5, 10):
    print(i)

# Print numbers from 5 to 9 with a step of 2 (5, 7, 9)
for i in range(5, 10, 2):
    print(i)

# -------------------------------
# LIST MODIFICATION BASED ON CONDITIONS
# -------------------------------

cities = {'Canada', 'New York', 'Chicago', 'America'}
mod_cities = []     # List to hold modified city names
upper_cities = []   # List to hold uppercase names of selected cities

print("Before mod cities:", mod_cities)  # Initially empty list

# Loop through each city and modify based on condition
for city in cities:
    if city != 'Chicago':
        mod_cities.append(city + 'UK')  # Append 'UK' to city name
    else:
        mod_cities.append(city)  # Keep 'Chicago' as is
        upper_cities.append(city.upper())  # Store uppercase version of 'Chicago'

print("After mod cities:", mod_cities)   # Show modified city list
print("After cities:", upper_cities)     # Show uppercase list (should contain 'CHICAGO')
