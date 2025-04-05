class Band:
    """A Band has a name and a list of Musicians."""

    def __init__(self, name):
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a Musician to the Band."""
        self.musicians.append(musician)

    def play(self):
        """Each musician in the band plays."""
        for musician in self.musicians:
            print(musician.play())

    def __str__(self):
        musician_list = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musician_list})"
