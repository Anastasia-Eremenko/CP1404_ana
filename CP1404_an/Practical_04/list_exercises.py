"""
Anastasia Eremenko
CP1404 - Practical
Prompting the user for numbers, displaying number analysis
"""
QUANTITY_OF_NUMBERS = 5
numbers = []

while len(numbers) < QUANTITY_OF_NUMBERS:
    try:
        number = int(input("Number: "))
        numbers.append(number)
    except ValueError:
        print("It has to be a number")
print(f"The first number is {numbers[0]}\nThe last number is {numbers[-1]}\nThe smallest number is {min(numbers)}\n"
      f"The largest number is {max(numbers)}\nThe average of the numbers is {sum(numbers)/len(numbers)}")