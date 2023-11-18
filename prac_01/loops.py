"""
3. Loops
"""
for i in range(1, 21, 2):
    print(i, end=' ')
print()
"""
a 
"""
for number in range(0, 101, 10):
    print(number, end=' ')
print()

"""
b
"""
for number in range(20, 0, -1):
    print(number, end=' ')
print()
"""
c
"""
# number_of_stars = int(input("Number of stars: "))
# for star in range(1, number_of_stars+1):
#     print("*", end='')
"""
d
"""
number_of_stars = int(input("Number of stars: "))
star_count = 1
for star in range(1, number_of_stars+1, 1):
    print("*"*star_count)
    star_count += 1
