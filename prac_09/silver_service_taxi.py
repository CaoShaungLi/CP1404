from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes fanciness."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness: float):
        """Initialise a Silver Service Taxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = fanciness * Taxi.price_per_km

    def __str__(self):
        """Return a string like a Taxi but with a flagfall."""
        return f"{super().__str__()} plus flagfall of {self.flagfall}"

    def get_fare(self):
        """Return the price for the taxi trip."""
        return super().get_fare() + self.flagfall
