"""
CP1404 - Practical
Paper code exercise for conversing passwords into *** 'stars'
"""


def main():
    """Converts a password string into "***" format"""
    password = str(input("Enter your password>> "))
    print_stars(password)


def print_stars(password):
    """Displays the stars equivalent to password length"""
    for i in range(len(password)):
        print("*", end="")


main()
