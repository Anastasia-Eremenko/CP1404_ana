"""
Prac 06 CP1404 - Languages Classes and OOP exercise: testing file
Expected time: 30min
Actual time: 34min
"""

from Practical_06.programming_language import ProgrammingLanguage


def main():
    """Program testing the ProgrammingLanguage class"""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)
    print()  # empty line

    # Create a list that contains three existing ProgrammingLanguage objects.
    languages = [python, ruby, visual_basic]
    for language in languages:
        print(language)
    print()  # empty line

    print("Dynamic languages:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)
