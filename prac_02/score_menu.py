MAX_SCORE = 100
MIN_SCORE = 0
EXCELLENT_THRESHOLD = 90
PASSABLE_THRESHOLD = 50


def main():
    score = get_valid_score()

    menu_running = True

    while menu_running:
        print("\nMenu:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")

        choice = input(">>> ").upper()

        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            print(score_result(score))
        elif choice == 'S':
            show_stars(score)
        elif choice == 'Q':
            print("Farewell!")
            menu_running = False
        else:
            print("Invalid option, please try again.")


def score_result(score):
    if score < MIN_SCORE or score > MAX_SCORE:
        return "Invalid score"
    elif score >= EXCELLENT_THRESHOLD:
        return "Excellent"
    elif score >= PASSABLE_THRESHOLD:
        return "Passable"
    else:
        return "Bad"


def get_valid_score():
    score = float(input("Enter score (0-100): "))
    while score < MIN_SCORE or score > MAX_SCORE:
        print(f"Invalid score. Please enter a score between {MIN_SCORE} and {MAX_SCORE}.")
        score = float(input("Enter score (0-100): "))
    return score


def show_stars(score):
    print('*' * int(score))


if __name__ == "__main__":
    main()
