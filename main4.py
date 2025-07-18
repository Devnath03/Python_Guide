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


#Boolean Expressions
if True:
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


if False:
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


