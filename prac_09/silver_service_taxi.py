from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes flag fall."""

    # Set up the flag fall price
    flag_fall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a Silver Service Taxi instance, based on parent class Taxi."""
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness
        super().__init__(name, fuel, fanciness)


    def get_fare(self):
        """Return the price add flag fall for the silver taxi trip."""
        return round(super().get_fare() + self.flag_fall, 2)

    def __str__(self):
        """Return a string like the taxi but with current fare distance and total price."""
        return f"{super().__str__()} plus flag fall of ${self.get_fare():.2f}"