"""
Prac 06 CP1404 - Guitar class operations :test file
Expected time: 20min
Actual time: 30min
"""
from Practical_06.guitar import Guitar

TITLE = "My guitars!"
guitars = []


def main():
    """Program that gets and processes user guitar info based on Guitar Class"""
    print(TITLE)
    while True:
        guitar_name = input("Name: ")
        if guitar_name == "":
            break
        guitar_year = get_valid_number("Year: ")
        guitar_cost = get_valid_number("Cost: ")
        guitar = Guitar(guitar_name, guitar_year, guitar_cost)
        print(f"{guitar} added")
        guitars.append(guitar)

    print_guitars()


def print_guitars():
    """Prints the list of guitars with their details."""
    for i, guitar in enumerate(guitars, 1):
        category = "(Vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:<20} ({guitar.year}), worth ${guitar.cost:10,.2f}{category}")


def get_valid_number(prompt):
    """Ensures the value entered is a number and is above 0"""
    while True:
        try:
            number = float(input(prompt))
            if number > 0:
                return number
            else:
                print("Number must be greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


main()
