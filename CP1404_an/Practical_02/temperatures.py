"""
CP1404 - Practical
Temperature conversion from prac 1
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""

print(MENU)
choice = input(">>> ").upper()
def main():
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = celcius_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celcius = fahrenheit_to_celcius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

def fahrenheit_to_celcius(f):
    c = 5 / 9 * (f - 32)
    return c


def celcius_to_fahrenheit(c):
    f = c * 9.0 / 5 + 32
    return f