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
    guitar_name = input("Name: ")
    while guitar_name != "":
        guitar_year = int(get_valid_number("Year: "))
        guitar_cost = get_valid_number("Cost: ")
        guitar = Guitar(guitar_name, guitar_year, guitar_cost)
        print(f"{guitar} added")
        guitar_name = input("Name: ")
        guitars.append(guitar)

    for i, guitar in enumerate(guitars):
        category = "(Vintage)" if guitar.is_vintage() else ""
        print(f"{i + 1} {guitar} {category}")


def get_valid_number(prompt):
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
