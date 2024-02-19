"""
CP1404 - Anastasia Eremenko
Paper code for a password stars
"""

MINIMUM_LENGTH = 4

def main():
    passowrd = get_passowrd()
    print_stars(passowrd)


def print_stars(passowrd):
    for i in range(len(passowrd)):
        print("*", end="")


def get_passowrd():
    passowrd = str(input("Enter your passowrd>> "))
    if len(passowrd) < MINIMUM_LENGTH:
        print("Invalid password")
        passowrd = get_passowrd()
    return passowrd


main()