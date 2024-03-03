"""
CP1404 - Practical Anastasia Eremenko
Files do from scratch task
"""

out_file = open('gitignore/data.txt', 'w') # Task part 0, creating the data file
out_file.close()

name = input("Name: ") # Task part 1, program that adds an input name to a file
out_file = open("gitignore/name.txt", "w")
print(name, file=out_file)
out_file.close()

with open("gitignore/name.txt", "r") as in_file:   # Task part 2, reads the names in name.txt, and displays them
    for line in in_file:
        print("Your name is", line)
in_file.close()

with open("gitignore/numbers.txt", "r") as in_file:   # Task part 3, reads the first two numbers in "numbers.txt", and adds them
    first_num = int(in_file.readline().strip())
    seccond_num = int(in_file.readline().strip())
    print(first_num + seccond_num)
in_file.close()

with open("gitignore/numbers.txt", "r") as in_file:   # Task part 4, reads all numbers in "numbers.txt", and adds them
    numbers = []
    for line in in_file:
        number = int(line.strip())
        numbers.append(number)
    print(sum(numbers))
in_file.close()