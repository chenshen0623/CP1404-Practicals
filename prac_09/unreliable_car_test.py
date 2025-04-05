from prac_09.unreliable_car import UnreliableCar

def test_unreliable_car():
    reliable_car = UnreliableCar("Mostly Reliable", 100, 90)
    unreliable_car = UnreliableCar("Barely Works", 100, 30)

    reliable_drives = 0
    unreliable_drives = 0
    test_runs = 100

    for _ in range(test_runs):
        if reliable_car.drive(1) > 0:
            reliable_drives += 1
        if unreliable_car.drive(1) > 0:
            unreliable_drives += 1

    print(f"Reliable car drove {reliable_drives} times out of {test_runs}")
    print(f"Unreliable car drove {unreliable_drives} times out of {test_runs}")

if __name__ == "__main__":
    test_unreliable_car()