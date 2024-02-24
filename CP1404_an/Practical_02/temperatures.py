"""
CP1404 - Practical
Temperature conversion from prac 1
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""



def main():
    """Menu based temperature converter program"""
    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()

    print("Thank you.")


def fahrenheit_to_celsius(f):
    """Converts a fahrenheit value to celsius"""
    c = 5 / 9 * (f - 32)
    return c


def celsius_to_fahrenheit(c):
    """Converts a celsius value to fahrenheit"""
    f = c * 9.0 / 5 + 32
    return f

main()