"""Intermediate Exercises"""
COLOUR_TO_CODE = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "Alice Blue": "#f0f8ff",
                  "Alizarin Crimson": "#e32636", "Amaranth": "#e52b50", "Amber": "#ffbf00", "Amethyst": "#9966cc",
                  "Antique White": "#faebd7", "Antique White1": "#ffefdb", "Antique White2": "#eedfcc"}
choice = input("Enter colour name: ").title()
while choice != "":
    if choice not in COLOUR_TO_CODE:
        print("Invalid choice")
    else:
        print(f"The colour code of {choice} is {COLOUR_TO_CODE[choice]}")
    choice = input("Enter colour name: ").title()
print("Finished")

