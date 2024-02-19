"""
CP1404 - Anastasia Eremenko
Paper code for a password stars
"""

MINIMUM_LENGTH = 4

passowrd = str(input("Enter your passowrd>> "))
if len(passowrd) < MINIMUM_LENGTH:
    print("Invalid password")
else:
    for i in range(len(passowrd)):
        print("*", end="")