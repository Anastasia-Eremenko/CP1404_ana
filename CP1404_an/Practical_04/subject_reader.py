"""
Anastasia Eremenko
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    all_parts = []
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        all_parts.append(parts) # storing all cleaned parts for later exercises
        print("----------")
    print(all_parts)  # Question 2 - display a nested list of all the names
    display_formated_part(all_parts) # Question 3 - Displays formatted parts
    input_file.close()

def display_formated_part(all_parts):
    """Displays a formatted string for each set of parts"""
    for part in all_parts:
        print(f"{part[0]} is taught by {part[1]:<12} and has {part[2]:>3} students")


main()