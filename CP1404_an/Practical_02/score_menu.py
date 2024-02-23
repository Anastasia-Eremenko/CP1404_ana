"""
CP1404 - Practical
Menu-driven score exercise
"""

MENU = """(G)et a valid score (must be 0-100 inclusive)
(P)rint result (copy or import your function to determine the result from score.py)
(S)how stars (this should print as many stars as the score)
(Q)uit"""


def main():
    """Menu driven program on setting,grading and displaying a score"""
    score = 0
    print(MENU)
    choice = get_valid_menu_choice()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        if choice == "P":
            result = determine_grade(score)
            print(f"{score}-{result}")
        if choice == "S":
            display_stars(score)
        print(MENU)
        choice = input(">>> ")
    print("Good bye")


def get_valid_menu_choice():
    """Identifies if the input menu choice is valid"""
    choice = input(">>> ").upper()
    while choice not in ["G", "P", "S", "Q"]:
        print("Invalid choice.")
        print(MENU)
        choice = input(">>> ").upper()
    return choice


def display_stars(score):
    """Displays * equal to the score"""
    for star in range(score):
        print("*", end="")
    print()


def get_valid_score():
    """Gets a valid score from the user"""
    score = int(input("What is your score?>>> "))
    if score > 100 or score < 0:
        print("Invalid score")
        int(input("What is your score?>>> "))
    return score


def determine_grade(score):
    """Determines the grade based on the user's input score"""
    if score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"


main()
