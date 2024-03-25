"""
Prac 07 CP1404 - Guitar exercise : client file
"""

from Practical_07.guitar import Guitar
import csv

FILENAME = "guitars.csv"


def main():
    guitars = load_data(FILENAME)
    guitars = sorted(guitars)
    print("Your current guitars:")
    for guitar in guitars:  # displays current guitars stored in the csv file
        print(guitar)
    add_guitar(guitars)  # user adds new guitars
    write_data(FILENAME, guitars)  # writes the data to an output csv file
    print("Your updated guitars:")
    for guitar in guitars:  # shows an updated version of stored guitars
        print(guitar)


def add_guitar(guitars):
    name = input("Enter guitar name (press enter to stop): ")
    while name != "":  # re prompts for more guitars until an empty name is entered
        year = get_valid_number("Enter year: ")  # if a float year is entered, it defaults to int
        cost = get_valid_number("Enter cost: ")
        guitars.append(Guitar(name, int(year), float(cost)))
        name = input("Enter guitar name (press enter to stop): ")


def get_valid_number(prompt):
    """Ensures the value entered is a number and is above 0"""
    while True:
        try:
            number = float(input(prompt))
            if number > 0:  # prevents the use of non-valid numbers
                return number
            else:
                print("Number must be greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def load_data(filename):
    guitars = []
    with open(filename, "r") as in_file:
        reader = csv.reader(in_file)
        for row in reader:
            guitar = Guitar(row[0], int(row[1]), float(row[2]))
            guitars.append(guitar)
    return guitars


def write_data(filename, guitars):
    with open(filename, "w", newline="") as out_file:
        writer = csv.writer(out_file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


if __name__ == "__main__":
    main()
