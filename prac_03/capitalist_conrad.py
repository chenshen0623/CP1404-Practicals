"""
CP1404/CP5632 - Practical
Capitalist Conrad wants a stock price simulator for a volatile stock.
The price starts off at $10.00, and, at the end of every day there is
a 50% chance it increases by 0 to 10%, and
a 50% chance that it decreases by 0 to 5%.
If the price rises above $1000, or falls below $0.01, the program should end.
The price should be displayed to the nearest cent (e.g. $33.59, not $33.5918232901)
"""
"""
import random

MAX_INCREASE = 0.1  # 10%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 0.01
MAX_PRICE = 1000.0
INITIAL_PRICE = 10.0

price = INITIAL_PRICE
print(f"${price:,.2f}")

while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # generate a random floating-point number
        # between negative MAX_DECREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    print(f"${price:,.2f}")
"""
MIN_PRICE = 1.0
MAX_PRICE = 1000.0
MAX_INCREASE = 0.175
MAX_DECREASE = 0.05
INITIAL_PRICE = 10.0
OUTPUT_FILE = "capitalist_conrad_output.txt"
import random

def main():
    """Simulate the random rise and fall of stock price in a given number of days,
    and stop if the price exceeds the specified range.
    The output result is written to a file."""

    number_of_days = int(input("How many days would you like to simulate? "))
    price = INITIAL_PRICE
    day_count = 0

    with open(OUTPUT_FILE, 'w') as out_file:
        print(f"Starting price: ${price:,.2f}", file=out_file)

        while day_count < number_of_days and MIN_PRICE <= price <= MAX_PRICE:
            day_count += 1

            if random.randint(1, 2) == 1:
                price_change = random.uniform(0, MAX_INCREASE)
            else:
                price_change = -random.uniform(0, MAX_DECREASE)

            price *= (1 + price_change)
            print(f"On day {day_count}: price is ${price:,.2f}", file=out_file)

    print(f"Simulation complete. Results written to {OUTPUT_FILE}.")

if __name__ == "__main__":
    main()
