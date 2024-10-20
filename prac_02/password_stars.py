"""
CP1404 Practical 2
Program to print asterisks based on user's password length
"""

MINIMUM_LENGTH = 8

def main():
    """Get password from user and print asterisks."""
    password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    """Print asterisks."""
    print('*' * len(password))


def get_password():
    """Get a valid password from user."""
    password = input("Enter a password: ")
    while len(password) < MINIMUM_LENGTH:
        print(f"Password must be at least {MINIMUM_LENGTH} characters long")
        password = input("Enter a password: ")
    return password


main()