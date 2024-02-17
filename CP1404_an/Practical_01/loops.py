"""
CP1404 -loops.py
"""

# example
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# Question a
for i in range(0, 101, 10):
    print(i, end=" ")
print()

# Question b
for i in range(20, 0, -1):
    print(i, end=" ")
print()

# Question c
for i in range(int(input("stars >>> "))):
    print("*" , end=" ")
print()

# Question d
for i in range(1, int(input("stars >>> "))):
    for m in range(i):
        print("*", end=" ")
    print()
