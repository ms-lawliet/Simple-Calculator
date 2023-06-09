# Create a Simple App Calculator
# 1.  The application will ask the user to choose one of the four math operations (Addition, Subtraction,
# Multiplication and Division)
# 2.  The application will ask the user for two numbers
# 3.  Display the result
# 4. The application will ask if the user wants to try again or not.
# 5. If yes, repeat Step 1.
# 6. If no, Display “Thank you!” and the program will exit
# 7. Use Python Function and appropriate Exceptions to capture errors during runtime.

import pyfiglet
import time
from colorama import Back

# create list of colors for font
red = '\033[91m'
green = '\033[92m'
blue = '\033[94m'
cyan = '\033[96m'
white = '\033[97m'
yellow = '\033[93m'
magenta = '\033[95m'
gray = "\033[37m"

# print program title
print(f"{yellow}+-*/"*185)
print(Back.BLACK + pyfiglet.figlet_format('Simple Calculator', font='lean', width=185, justify='center'),
      end='')
print(Back.RESET + f"{yellow}+-*/"*185)
time.sleep(0.5)


def simple_calc():
    while True:
        # ask user for operation
        operation = input(Back.BLACK + f"{red}Enter operation to be used: ").lower()
        operations = ["addition", "subtraction", "multiplication", "division"]

        if operation not in operations:
            raise Exception("Invalid operation.")
        else:
            # ask user for two numbers
            try:
                num1 = int(input(Back.BLACK + f"{green}Enter first number: "))
                num2 = int(input(Back.BLACK + f"{green}Enter second number: "))
            except ValueError:
                print(Back.RESET + f"{red}Input is not an integer. Please try again.")
            else:
                # perform operation then display result
                # for addition,
                if operation == operations[0]:
                    add = num1 + num2
                    print(Back.RESET + f"{magenta}{num1} + {num2} = {add}")
                # for subtraction,
                elif operation == operations[1]:
                    difference = num1 - num2
                    print(Back.RESET + f"{blue}{num1} - {num2} = {difference}")
                # for multiplication,
                elif operation == operations[2]:
                    product = num1 * num2
                    print(Back.RESET + f"{cyan}{num1} * {num2} = {product}")
                # for division
                elif operation == operations[3]:
                    try:
                        quotient = num1 / num2
                        print(Back.RESET + f"{gray}{num1} + {num2} = {quotient}")
                    except ZeroDivisionError:
                        print(Back.RESET + f"{red}Division by Zero Error. Try again.")

                # ask user if there are more
                repeat = input(Back.BLACK + f"{yellow}Do you want to try again? (yes or no) ").lower()
                choices = ["yes", "no"]
                if repeat not in choices:
                    raise Exception("Yes or no only.")
                else:
                    # if yes,
                    # repeat process
                    if repeat == "yes":
                        continue
                    # if no,
                    # display "Thank and you" and exit
                    else:
                        print(Back.RESET + f"{white}Thank you! ")
                        break


simple_calc()
