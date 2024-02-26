import random

print(dir(random))
help(random.randint)
help(random.randrange)


print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# What did you see on line 1?
# What was the smallest number you could have seen, what was the largest?
""" Smallest number: 5, the largest number:20.
Output includes all integer values from 5-20 (inclusive) """

# What did you see on line 2?
# What was the smallest number you could have seen, what was the largest?
""" Smallest number 3, The Largest number: 9
Output includes integer values between 3 and 10 in steps of two
Therefore the maximum number achievable is 9  since 3 + 2(3) = 9 """

# Could line 2 have produced a 4?
" No, since 3 != 4 and the first step = 5 "

# What did you see on line 3?
# What was the smallest number you could have seen, what was the largest?
""" Smallest: 2.5, Largest: 5.5
Line 3 returns a random float between 2.5 to 5.5 inclusive """

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1, 100))
