from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

print("Let's Drive!")
MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    """The main program of taxi simulator."""

    # Welcome message
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    bill = 0
    current_taxi = None

    choice = input(f"{MENU}\n>>>").lower()
    while choice != "q":
        if choice == "c":
            current_taxi = choose_taxi(taxis)
        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive.")
            else:
                bill += drive_taxi(current_taxi)
                print(f"Bill to date: ${bill:.2f}")
        else:

            print("Invalid option")
        choice = input(f"{MENU}\n>>>").lower()

    print(f"Total trip cost: ${bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def choose_taxi(taxis):
    """Display available taxis and let the user choice one taxi and return it."""
    print("Taxis available:")
    display_taxis(taxis)

    try:
        choice = int(input("Taxis available: "))
        if 0 <= choice < len(taxis):
            return taxis[choice]
        else:
            print("Invalid taxi choice")
    except ValueError:
        print("Invalid input")

def drive_taxi(current_taxi):
    """"Ask the user how far to drive and calculate the trip cost and return distance."""
    try:
        distance = float(input("Drive how far? "))
        current_taxi.start_fare()
        current_taxi.drive(distance)
        fare = current_taxi.get_fare()
        print(f"Your {current_taxi.name} trip cost you ${fare:.2f}")
        return fare
    except ValueError:
        print("Invalid input. Please enter a number.")
        return 0