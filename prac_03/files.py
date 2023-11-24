# OUT_FILE = "name.txt"
# name = input("Enter name: ")
# out_file = open("OUT_FILE", 'w')
# print(name, file=out_file)
# out_file.close()
#
# IN_FILE = "name.txt"
# in_file = open("IN_FILE", 'r')
# text = in_file.read()
# print(f"Your name is {text}")
# in_file.close()

IN_FILE = "numbers.txt"
total = 0
with open(IN_FILE) as in_file:
    for i in range(2):
        value = in_file.readline()
        total += int(value)
    print(int(total))

# IN_FILE = "numbers.txt"
# with open(IN_FILE) as in_file:
#     for line in in_file:
#         number = str(line)
#         print(number.strip())
