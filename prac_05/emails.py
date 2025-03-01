"""
emails.py

Estimate: 30 minutes
Actual: 40 minutes
"""
def main():
    """Get user's email address and name to print
    ,and print name and email."""
    email_to_name = {}
    email = input("Email: ").strip()

    while email:
        guessed_name = extract_name(email)
        confirmation = input(f"Is your name {guessed_name}? (Y/n) ").strip().lower()

        if confirmation not in ('y', ''):
            guessed_name = input("Name: ").title()
        email_to_name[email] = guessed_name
        email = input("Email: ").strip()

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    """Extract a probable name from an email."""
    local_part = email.split('@')[0]
    name = local_part.replace('.', ' ').title()
    return name

main()
