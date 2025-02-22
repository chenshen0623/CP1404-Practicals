def main():
    """The main function calls the function to execute the program."""
    number_of_numbers = 5
    numbers = get_numbers(number_of_numbers)
    display_number_statistics(numbers)
    check_username()

def get_numbers(number_of_numbers):
    """Gets the specified number of numbers entered by the user and returns a list."""
    numbers = []
    for _ in range(number_of_numbers):
        number = int(input("Number: "))
        numbers.append(number)
    return numbers


def display_number_statistics(numbers):
    """Calculates and displays statistics for a list of numbers."""
    print(f"The first number is {numbers[0]}\n"
          f"The last number is {numbers[-1]}\n"
          f"The smallest number is {min(numbers)}\n"
          f"The largest number is {max(numbers)}\n"
          f"The average of the numbers is {sum(numbers) / len(numbers)}")


def check_username():
    """Check that the username entered by the user is in the list."""
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
                 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
                 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

    username = input("Username: ")
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")


main()