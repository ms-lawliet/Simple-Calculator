# Create a Simple App Calculator
# 1.  The application will ask the user to choose one of the four math operations (Addition, Subtraction,
# Multiplication and Division)
# 2.  The application will ask the user for two numbers
# 3.  Display the result
# 4. The application will ask if the user wants to try again or not.
# 5. If yes, repeat Step 1.
# 6. If no, Display “Thank you!” and the program will exit
# 7. Use Python Function and appropriate Exceptions to capture errors during runtime.

# ask user for operation
operation = input("Enter operation to be used: ").lower()
operations = ["addition", "subtraction", "multiplication", "division"]
# ask user for two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
# perform operation then display result
# for addition,
if operation == operations[0]:
    add = num1 + num2
    print(f"{num1} + {num2} = {add}")
# for subtraction,
elif operation == operations[1]:
    difference = num1 - num2
    print(f"{num1} - {num2} = {difference}")
# ask user if there is more
# if yes,
# repeat process
# if no,
# display "Thank and you" and exit
