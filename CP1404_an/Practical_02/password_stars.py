"""
CP1404 - Practical
Paper code for a password stars
"""


def main():
    password = str(input("Enter your password>> "))
    print_stars(password)


def print_stars(password):
    for i in range(len(password)):
        print("*", end="")


main()
