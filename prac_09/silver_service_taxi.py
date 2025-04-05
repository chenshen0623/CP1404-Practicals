from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes flag fall."""

    # Set up the flag fall price
    flag_fall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a Silver Service Taxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness
