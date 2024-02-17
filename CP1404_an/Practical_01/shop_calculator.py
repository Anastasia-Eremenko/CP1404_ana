"""
CP1404 - shop_calculator.py
"""

total = 0
number_of_items = int(input("How many items?: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("How many items?: "))
for i in range(number_of_items):
    item_price = float(input(f"Price for item {i+1}: "))
    total += item_price
print(f"Your total price for {number_of_items} items is ${total:.2f}")