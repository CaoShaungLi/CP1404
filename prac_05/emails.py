"""Emails"""
email_to_name = {}
email = input("Email: ")
while email != "":
    name = email.split("@")[0]
    name_parts = name.split(".")
    full_name = " ".join(name_parts).title()
    # print(name)
    # print(name_parts)
    # print(full_name)
    choice = input(f"Is your name {full_name}? (Y/n) ").lower()
    if choice != "y" and choice != "":
        full_name = input("Name: ")
    email_to_name[full_name] = email
    print(email_to_name)
    email = input("Email: ")
for full_name, email in email_to_name.items():
    print(f"{full_name} ({email})")


