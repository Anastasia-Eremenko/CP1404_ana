"""
Anastasia Eremenko
CP1404 - Practical
Basic list operations and Woefully inadequate security checker
"""

# Basic list operations

QUANTITY_OF_NUMBERS = 5
numbers = []

while len(numbers) < QUANTITY_OF_NUMBERS:
    try:
        number = int(input("Number: "))
        numbers.append(number)
    except ValueError:
        print("It has to be a number")
print(f"The first number is {numbers[0]}\nThe last number is {numbers[-1]}\nThe smallest number is {min(numbers)}\n"
      f"The largest number is {max(numbers)}\nThe average of the numbers is {sum(numbers) / len(numbers)}")

"""


"""

# Woefully inadequate security checker
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']


def main():
    """A program that grants access based on valid usernames"""
    while True:  # program modified to repeatedly ask, until a correct user is entered
        name = input("username: ")
        if check_if_valid_user(name):
            print("Access granted")
            break
        else:
            print("Access denied")


def check_if_valid_user(name):
    """Check if the username is valid"""
    access = False
    for valid_user in usernames:
        if valid_user == name:
            access = True
    return access


main()
