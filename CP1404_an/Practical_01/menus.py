"""
CP1404 - menus.py
"""

name = input("Enter Name: ")
print("(H)ello\n(G)oodbye\n(Q)uit")
choice = input("Choice: ").upper()
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid")
    print()
    print("(H)ello\n(G)oodbye\n(Q)uit")
    choice = input("Choice: ").upper()
print("Finished")
