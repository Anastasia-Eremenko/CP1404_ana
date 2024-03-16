"""
CP1404 Practical
Email storing program - do from scratch exercise
"""

VALID_EMAIL_TYPES = ["jcu.edu.au", "gmail.com", "hotmail.com"]
emails = {}


def main():
    email = input("please enter your email: ")
    while email != "":
        if valid_email_format(email):
            email_parts = email.split("@")
            name_parts = " ".join(email_parts[0].split(".")).title()
            name_like_email = input(f"Is your name {name_parts}? (y/n): ").lower()
            if name_like_email == "y":
                name = name_parts
            else:
                name = input("Enter your name:")
            emails[email] = name
        else:
            print("email is not valid, must contain only 1 @, and be a valid email type")
        email = input("please enter your email: ")
    for name, email in emails.items():
        print(f"{name} {email}")


def valid_email_format(email):
    if email.count("@") != 1:
        return False
    if email.split("@")[1] in VALID_EMAIL_TYPES:
        return True


main()
