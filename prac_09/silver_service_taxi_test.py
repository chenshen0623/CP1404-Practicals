from prac_09.silver_service_taxi import SilverServiceTaxi

def main():
    """Test for SilverServiceTaxi class"""

    # Set the name, fuel and fanciness
    hummer = SilverServiceTaxi("Hummer", 200, 2)
    hummer.drive(18)
    print(hummer)

if __name__ == '__main__':
    main()