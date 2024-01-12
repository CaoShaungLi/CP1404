"""Band class for CP2404"""


class Band:
    """Band class"""

    def __init__(self, name=""):
        """Construct a Band with a name and empty musician collection."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band."""
        return f"{self.name} ({','.join([str(musician) for musician in self.musicians])})"

    def __repr__(self):
        """Return a string representation of a Band."""
        return str(self)

    def add(self, musician):
        """Add a musician to band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing the musician playing their first (or no) musician."""
        if not self.musicians:
            return f"{self.name} needs a musician!"
        return '\n'.join([musician.play() for musician in self.musicians])

