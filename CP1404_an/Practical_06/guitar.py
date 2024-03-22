"""
Prac 06 CP1404 - Guitar exercise : class file
Expected time: 40min
Actual time: 35min
"""


CURRENT_YEAR = 2024
VINTAGE_THRESHOLD = 50  # minimum number of years to be considered vintage


class Guitar:
    """Represents a Guitar object"""
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):  # Gibson L-5 CES (1922) : $16,035.40 string formatting
        """Guitar object attributes formatted as a string"""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):  # gets how old the guitar is
        """Determines the current age of the guitar"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determines if the guitar is vintage based on its age"""
        return self.get_age() >= VINTAGE_THRESHOLD
