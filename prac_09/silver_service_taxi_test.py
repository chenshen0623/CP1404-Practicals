from prac_09.silver_service_taxi import SilverServiceTaxi

def main():
    """Test for SilverServiceTaxi class"""

    # Set the name, fuel and fanciness
    hummer = SilverServiceTaxi("Hummer", 200, 2)
    hummer.start_fare()
    hummer.drive(18)
    print(hummer)
    print(f"Total fare: ${hummer.get_fare():.2f}")  # 明确输出车费

if __name__ == '__main__':
    main()