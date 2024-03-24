"""
Prac 07 CP1404 - Guitar exercise : client file
"""

from Practical_07.guitar import Guitar
import csv


FILENAME = "guitars.csv"

def main():
    guitars = load_data(FILENAME)
    guitars = sorted(guitars)
    for guitar in guitars:
        print(guitar)


def load_data(filename):
    guitars = []
    with open(filename, "r") as in_file:
        reader = csv.reader(in_file)
        for row in reader:
            guitar = Guitar(row[0], row[1], float(row[2]))
            guitars.append(guitar)
    return guitars


if __name__ == "__main__":
    main()