MINIMUM_PASSWORD_LENGTH = 10


def main():
    password = get_password()
    while len(password) < MINIMUM_PASSWORD_LENGTH:
        print("Invalid password, should be at least 10 characters")
    password = get_password()
    display_asterisks(password)


def display_asterisks(password):
    print("Password: ", "*" * len(password))


def get_password():
    password = input("Enter password: ")
    return password


main()
