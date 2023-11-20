"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random

"""
2. Debugging
"""
MINIMUM_THRESHOLD = 0
MAXIMUM_THRESHOLD = 100
PASSABLE_THRESHOLD = 50
EXCELLENT_THRESHOLD = 90


def main():
    """Get score and print result from score and random scores."""
    score = get_valid_score()
    result = determine_grade(score)
    print(result)
    random_score = random.uniform(MINIMUM_THRESHOLD, MAXIMUM_THRESHOLD)
    random_score_result = determine_grade(random_score)
    print(f"Random score: {random_score}")
    print(random_score_result)


def get_valid_score():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
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


main()
