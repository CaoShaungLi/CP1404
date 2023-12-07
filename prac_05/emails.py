"""Emails"""

PREFIX = 0
email_to_name = {}


def main():
    """Get email and display name from email"""
    email = input("Email: ")
    while email != "":
        full_name = extract_name_from_email(email)
        is_your_name(email, full_name)
        print(email_to_name)
        email = input("Email: ")
    for full_name, email in email_to_name.items():
        print(f"{full_name} ({email})")


def is_your_name(email, full_name):
    """Determine if the name from email is your name"""
    choice = input(f"Is your name {full_name}? (Y/n) ").lower()
    if choice != "y" and choice != "":
        full_name = input("Name: ")
    email_to_name[full_name] = email


def extract_name_from_email(email):
    """Extract name from email"""
    name = email.split("@")[PREFIX]
    name_parts = name.split(".")
    full_name = " ".join(name_parts).title()
    return full_name


main()
