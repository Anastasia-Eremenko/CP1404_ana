"""
CP1404 - Practical
Menu-driven score exercise
A menu based program that obtains a user score and attributes a grade or achievement level
"""

MENU = """(G)et a valid score (must be 0-100 inclusive)
(P)rint result (copy or import your function to determine the result from score.py)
(S)how stars (this should print as many stars as the score)
(Q)uit"""
EXCELLENT_THRESHOLD = 90  # sets the minium values for passing or excellency
PASSABLE_THRESHOLD = 50


def main():
    """Menu-driven program on setting,grading and displaying a score"""
    score = 0  # sets initial score to a non NULL value
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
        choice = get_valid_menu_choice()
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
    """Displays * repetitions equal to the score"""
    print("*" * score)


def get_valid_score():
    """Gets a valid score from the user"""
    while True:
        score = int(input("What is your score?>>> "))
        if 0 <= score <= 100:
            return score
        else:
            print("Invalid score. Please enter a score between 0 and 100.")


def determine_grade(score):
    """Determines the grade based on the user's input score"""
    if score >= EXCELLENT_THRESHOLD:
        return "Excellent"
    elif score >= PASSABLE_THRESHOLD:
        return "Passable"
    else:
        return "Bad"


main()
