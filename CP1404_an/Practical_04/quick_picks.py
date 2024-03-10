"""
Anastasia Eremenko
CP1404 - Practical
Quick picks do from scratch exercise
"""
import random

QTT_OF_NUMBERS_PER_PICK = 6
MIN_NUM = 1
MAX_NUM = 45


def main():
    """Generates a set of non reoccurring quick picks"""
    num_of_picks = int(input("How many picks?: "))
    for i in range(num_of_picks):
        picks = get_quick_picks()
        display_picks(picks)


def get_quick_picks():
    """Generate a single line of sorted quick picks"""
    numbers = []
    for i in range(QTT_OF_NUMBERS_PER_PICK):
        number = random.randint(MIN_NUM, MAX_NUM)
        while number in numbers:
            number = random.randint(MIN_NUM, MAX_NUM)
        numbers.append(number)
    return sorted(numbers)


def display_picks(picks):
    """Formats and displays the picks"""
    for pick in picks:
        print(f"{pick:>2}", end=" ")
    print()


main()
