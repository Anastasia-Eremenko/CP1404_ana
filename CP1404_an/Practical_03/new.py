"""
(OPENS A FILE FOR READING)
FILENAME = "texts.txt"
in_file = open(FILENAME)
for line in in_file:
    print(line.strip())
in_file.close

with open(FILENAME, "r") as in_file:
    for line in in_file:
    print(line)

(OPENS A FILE AND APPENDS A NAME, V1 AND V2)
name = input("Name: ")
out_file = open("name.txt", "a")
print(name, file=out_file)
out_file.close()


name = input("Name: ")
with open(FILENAME, "a") as out_file:
    out_file.write(name)
"""

FILENAME = "guitars.txt"
with open(FILENAME, "r") as in_file:
    for line in in_file:
        parts = line.strip().split(",")
        name = parts[0].strip()
        year = parts[1].strip()
        price = parts[2].strip()
        print(name, year, price[0:-2])

