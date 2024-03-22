"""
Prac 06 CP1404 - Languages Classes and OOP exercise: class file
Expected time: 30min
Actual time: 34min
"""

class ProgrammingLanguage:
    """Represents a ProgrammingLanguage object"""
    def __init__(self, name= "", typing="/",reflection= "/",year = 0):
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.name = name

    def is_dynamic(self):
        """Determines boolean if language is dynamic"""
        if self.typing.title() == "Dynamic":
            return True
        else:
            return False

    def __str__(self):
        """ProgrammingLanguage object attributes formatted as a string"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
