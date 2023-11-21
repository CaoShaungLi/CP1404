# import random
#
# print(random.randint(5, 20))  # line 1
# print(random.randrange(3, 10, 2))  # line 2
# print(random.uniform(2.5, 5.5))  # line 3
# What did you see on line 1?
# 20
# What was the smallest number you could have seen, what was the largest?
# smallest number - 5, largest number - 20
# What did you see on line 2?
# 9
# What was the smallest number you could have seen, what was the largest?
# smallest number - 3, largest number - 9
# Could line 2 have produced a 4?
# No because the smallest number is 3 with step 2.
# What did you see on line 3?
# 3.4273078962357326
# What was the smallest number you could have seen, what was the largest?
# smallest number - 2.5, largest number - 5.5

"""
Write code, not a comment, to produce a random number between 1 and 100 inclusive.
"""
import random

print(random.uniform(1, 100))
