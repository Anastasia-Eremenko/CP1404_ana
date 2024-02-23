"""
CP1404 - Practical
Broken score from prac 1
"""

import random


def main():
    """A program that receives a user score and grades it"""
    score = get_score()
    print(score)
    determine_grade(score)
    rand_score = get_random_score()
    print(rand_score)
    determine_grade(rand_score)


def determine_grade(score):
    """Determines the grade status based on the user's input score"""
    if score < 0 or score > 100:
        print("Invalid score")
    else:
        if score > 90:
            print("Excellent")
        elif score > 50:
            print("Passable")
        else:
            print("Bad")


def get_score():
    """Attains a score input from the user"""
    score = int(input("Enter score: "))
    return score


def get_random_score():
    """Attains a random valid score 0-100"""
    score = random.randint(0, 100)
    return score


main()
