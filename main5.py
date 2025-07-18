# While loop
# A while loop is a control structure in Python that repeats a block of code as long as a condition is true.
# Example 1: Print "Hello" five times using a while loop
x = 1
while (x <= 5):
    print("Hello")   # prints "Hello"
    x = x + 1        # increment x by 1 after each iteration

# Example 2: Print numbers from 1 to 10
initial = 1
while initial <= 10:
    print(initial)   # prints the current value of 'initial'
    initial += 1     # increment 'initial' by 1

# Example 3: Calculate the sum of the first 'n' positive integers
n = int(input("Enter a Integer no Here : "))  # take user input and convert to integer

sum = 0   # initialize sum to 0
i = 1     # initialize counter to 1
while i <= n:
    sum = sum + i   # add current value of i to sum
    i = i + 1       # increment i by 1
print("The sum of the first", n, "positive integers is:", sum)

# Example 4: Password check using while loop
correct_password = "1234"                     # predefined correct password
password = input("Enter your password : ")    # prompt user to enter password
while password != "1234":                     # loop runs as long as password is incorrect
    print("Incorrect Password")               # notify user
    password = input("Enter your password : ")# ask again
print("Password Correct")                     # printed after correct password is entered

# ---------------------------------------------------------------
#           For Loops & While Loops — Key Differences
# ---------------------------------------------------------------
# | Feature       | For Loop                                  | While Loop                                  |
# |---------------|-------------------------------------------|---------------------------------------------|
# | Purpose       | Used when the number of iterations        | Used when the number of iterations          |
# |               | is known.                                 | is unknown.                                 |
# |---------------|-------------------------------------------|---------------------------------------------|
# | Syntax        | for item in sequence:                     | while condition:                            |
# |               |     # Code                                |     # Code                                  |
# |---------------|-------------------------------------------|---------------------------------------------|
# | Control       | Iterates over a sequence (range, list,    | Continues as long as the condition is True  |
# |               | etc.)                                     |                                             |
# |---------------|-------------------------------------------|---------------------------------------------|
# | Termination   | Ends when the sequence is exhausted.      | Ends when the condition becomes False.      |
# |---------------|-------------------------------------------|---------------------------------------------|
# | Example       | for i in range(5):                        | count = 0                                   |
# |               |     print(i)                              | while count < 5:                            |
# |               |                                           |     print(count)                            |
# |---------------|-------------------------------------------|---------------------------------------------|
# | When to Use   | When you know how many times to loop.     |When you don’t know the number of iterations.|
# ----------------------------------------------------------------------------------------------------------

#Break Statement
# Break Mean