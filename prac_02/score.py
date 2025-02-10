import random

MAX_SCORE = 100
MIN_SCORE = 0
EXCELLENT_THRESHOLD = 90
PASSABLE_THRESHOLD = 50

def main():
    score = float(input("Enter score: "))
    print(score_result(score))
    random_score = random.uniform(MIN_SCORE, MAX_SCORE)
    print(f"Random score: {random_score:.2f}")
    print(score_result(random_score))

def score_result(score):
    if score < MIN_SCORE or score > MAX_SCORE:
        return "Invalid score"
    elif score >= EXCELLENT_THRESHOLD:
        return "Excellent"
    elif score >= PASSABLE_THRESHOLD:
        return "Passable"
    else:
        return "Bad"

main()
