"""
CP1404 - Prac 5
Program: Emails
"""

def main():
    """Create dictionary of emails to names, and displays it."""
    email_to_name = {}
    email = input('Email: ')

    while email != "":
        name = extract_name(email)
        name_confirmation = input(f"Is your name {name}? (Y/n) ").upper()
        if name_confirmation != "" and name_confirmation != "Y":
            name = input("Name: ").title()
        email_to_name[email] = name
        email = input('Email: ')

    for email, name in email_to_name.items():
        print(f"{name} ({email})")

def extract_name(email):
    """Extract name from email."""
    unformatted_name = email.split('@')[0]
    name = " ".join(unformatted_name.split('.')).title()
    return name

main()
