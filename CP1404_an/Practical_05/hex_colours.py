"""
CP1404 Practical
Colour names and codes in a dictionary
"""

colors_dict = {"absolute zero": "#0048ba", "acid green": "#b0bf1a", "alice blue": "#f0f8ff",
               "alizarin crimson": "#e32636", "amaranth": "#e52b50", "amber": "#ffbf00",
               "amethyst": "#9966cc", "antique white": "#faebd7", "antique white 1": "#ffefdb",
               "antique white 2": "#eedfcc", "antique white 3": "#cdc0b0", "antique white4": "#8b8378",
               "apricot": "#fbceb1", "aqua": "#00ffff"}
# since dictionary key lookup is case-sensitive, the dictionary provided is lower-case
# alternatively this can be done by creating a new dictionary with only upper or lower color names

def main():
    """A program that converts a color name to its colour code"""
    colour = input("Enter a colour: ").lower()
    while colour != "":
        try:
            print(f"{colour.capitalize()} is {colors_dict[colour]}")
        except KeyError:
            print("This is not a valid colour name")
        colour = input("Enter a colour: ").lower()


main()
