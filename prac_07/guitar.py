CURRENT_YEAR = 2024
VINTAGE_YEAR = 50


class Guitar:
    """provide details about a guitar."""
    def __init__(self, name='', year=0, cost=0.0):
        """Initialise the guitar."""
        self.name = name
        self.year = year
        self.cost = cost