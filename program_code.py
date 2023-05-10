# Create a Simple App Calculator
# 1.  The application will ask the user to choose one of the four math operations (Addition, Subtraction,
# Multiplication and Division)
# 2.  The application will ask the user for two numbers
# 3.  Display the result
# 4. The application will ask if the user wants to try again or not.
# 5. If yes, repeat Step 1.
# 6. If no, Display “Thank you!” and the program will exit
# 7. Use Python Function and appropriate Exceptions to capture errors during runtime.

while True:
    # ask user for operation
    operation = input("Enter operation to be used: ").lower()
    operations = ["addition", "subtraction", "multiplication", "division"]

    if operation not in operations:
        raise Exception("Invalid operation.")
    else:
        # ask user for two numbers
        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
        except ValueError:
            print("Input is not an integer. Please try again.")
        else:
            # perform operation then display result
            # for addition,
            if operation == operations[0]:
                add = num1 + num2
                print(f"{num1} + {num2} = {add}")
            # for subtraction,
            elif operation == operations[1]:
                difference = num1 - num2
                print(f"{num1} - {num2} = {difference}")
            # for multiplication,
            elif operation == operations[2]:
                product = num1 * num2
                print(f"{num1} * {num2} = {product}")
            # for division
            elif operation == operations[3]:
                quotient = num1 / num2
                print(f"{num1} + {num2} = {quotient}")

            # ask user if there is more
            repeat = input(f"Do you want to try again? (yes or no) ").lower()
            # if yes,
            # repeat process
            if repeat == "yes":
                continue
            # if no,
            # display "Thank and you" and exit
            else:
                print(f"Thank you! ")
                break
