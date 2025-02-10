def main():
    password = get_password()
    print_asterisks(password)

def get_password():
    password = input("Enter your password: ")
    while len(password) < 8:
        print("Password must be at least 8 characters long.")
        password = input("Enter your password: ")
    return password

def print_asterisks(password):
    print('*' * len(password))

main()
