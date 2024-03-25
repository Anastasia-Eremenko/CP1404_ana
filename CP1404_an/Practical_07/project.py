"""
CP1404 - Project exercice
Time estimate: 40 mins
Actual time:
"""

from datetime import datetime


class Project:
    """Class that holds project information"""
    def __init__(self, name="", start_date="", priority=0, estimate_cost=0, completion=0):
        self.name = name
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y")  # Store date as date object
        self.priority = priority
        self.estimate_cost = estimate_cost
        self.completion_percentage = completion

    def __str__(self):
        """Display project details with corrected formatting"""
        return f"{self.name}, start: {self.start_date.strftime('%Y/%m/%d')}, priority {self.priority}, estimate: " \
               f"${self.estimate_cost}, completion: {self.completion_percentage}%"

    def __lt__(self, other):
        """Sets project ranking and sorting to list by priority value"""
        return self.priority < other.priority

    def new_percentage(self, percentage):
        """Changes the percentage to the new value"""
        self.completion_percentage = percentage

    def update_priority(self, priority):
        """Updates the priority of the project"""
        self.priority = priority

    def compare_date(self, filter_date):
        """Boolean comparison of the date with an inputted user date"""
        filter_date = datetime.strptime(filter_date, "%d/%m/%Y")
        return self.start_date >= filter_date