"""
Prac 06 CP1404 - Guitars exercise: testing file
Expected time: 40min
Actual time: 25min
"""

from Practical_06.guitar import Guitar


def main():
    """A program that tests attributes of Guitar class """
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)  # defining guitar parameters
    unknown_guitar = Guitar("Unknown Guitar", 2013)
    print(gibson)
    print(unknown_guitar)
    print()

    # Manual testing
    # Expected year values have been adjusted to fit year = 2024
    print(f"Gibson L-5 CES get_age() - Expected 102. Got {gibson.get_age()}")
    print(f"Another Guitar get_age() - Expected 11. Got {unknown_guitar.get_age()}")
    print(f"Gibson L-5 CES is_vintage() - Expected True. Got {gibson.is_vintage()}")
    print(f"Another Guitar is_vintage() - Expected False. Got {unknown_guitar.is_vintage()}")


main()
