import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICK = 6


def main():
    """Print a number of lines with randomly chosen numbers in increasing order."""
    number_of_picks = int(input("How many quick picks? "))
    for i in range(number_of_picks):
        random_numbers = pick_numbers()
        print(" ".join(f"{number:2}" for number in sorted(random_numbers)))


def pick_numbers():
    """Pick random, non-repeated numbers and put them in a list."""
    random_numbers = []
    for x in range(NUMBERS_PER_PICK):
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        while number in random_numbers:
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
        random_numbers.append(number)
    return sorted(random_numbers)


main()