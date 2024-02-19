"""
CP1404 - sequences.py
extension
"""

MENU = "1) Show the even numbers from x to y\n2) Show the odd numbers from x to y\n3) Show the squares from x to y 4)" \
       "\n4) Exit the program"


def main():
    print(MENU)
    option = int(input("Choose option 1-4 >>> "))
    while option != 4:
        if option == 1:
            even_exercise()
        if option == 2:
            odd_exercise()
        if option == 3:
            square_exercise()
        print(MENU)
        option = int(input("Choose option 1-4 >>> "))
    print("BYE BYE!")




def even_exercise():
    print("Lets find the even numbers!")
    start_number = int(input("Starting number?: "))
    end_number = int(input("Ending number?: "))
    numbers = []
    for number in range(start_number, end_number + 1):
        if number % 2 == 0:
            numbers.append(number)
    print(numbers)


def odd_exercise():
    print("Lets find the odd numbers!")
    start_number = int(input("Starting number?: "))
    end_number = int(input("Ending number?: "))
    numbers = []
    for number in range(start_number, end_number + 1):
        if number % 2 == 1:
            numbers.append(number)
    print(numbers)


def square_exercise():
    print("Lets find the squares numbers!")
    start_number = int(input("Starting number?: "))
    end_number = int(input("Ending number?: "))
    numbers = []
    for number in range(start_number, end_number + 1):
        number = int(number) ** 2
        numbers.append(number)
    print(numbers)

main()