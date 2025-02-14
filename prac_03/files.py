def main():
    print("Program 1")
    program_1()

    print("\nProgram 2")
    program_2()

    print("\nProgram 3")
    program_3()

def program_1():
    """
    Ask the user's name and write it in name.txt.
    Read the contents in name.txt and print it out.
    """
    name = input("Enter your name: ")

    file_out = open("name.txt", "w")
    file_out.write(name)
    file_out.close()

    file_in = open("name.txt", "r")
    stored_name = file_in.read()
    file_in.close()

    print(f"Your name is {stored_name}")


def program_2():
    """
    Read the first two lines of numbers in the numbers.txt file and add them up.
    """
    with open("numbers.txt", "r") as file_in:
        first_line = file_in.readline()
        second_line = file_in.readline()

    total = int(first_line) + int(second_line)
    print(f"The sum of the first two numbers is: {total}")


def program_3():
    """
    Read all the lines in the numbers.txt file and sum them up.
    """
    total = 0
    with open("numbers.txt", "r") as file_in:
        for line in file_in:
            number = int(line)
            total += number

    print(f"The total of all numbers in numbers.txt is: {total}")

main()