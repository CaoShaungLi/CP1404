MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"
MAXIMUM_SCORE = 100
MINIMUM_SCORE = 0
PASSABLE_THRESHOLD = 50
EXCELLENT_THRESHOLD = 90
DEFAULT_SCORE = -1


def main():
    score = DEFAULT_SCORE
    """Get score, determine grade, and print stars for user."""
    print(MENU)
    choice = input("choice: ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            if score == DEFAULT_SCORE:
                print("No score entered, please get score first")
                score = get_valid_score()
            result = determine_grade(score)
            print(result)
        elif choice == "S":
            if score == DEFAULT_SCORE:
                print("No score entered, please get score first")
                score = get_valid_score()
            display_stars(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input("choice: ").upper()
    print("Farewell")


def get_valid_score():
    """Get a valid score from user."""
    score = float(input("Enter score: "))
    while score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score


def determine_grade(score):
    """Determine grade from user's score."""
    if score < PASSABLE_THRESHOLD:
        result = "Bad"
    elif score < EXCELLENT_THRESHOLD:
        result = "Passable"
    else:
        result = "Excellent"
    return result


def display_stars(score):
    """Display stars according to number of user's score."""
    print("*" * int(score))


main()
