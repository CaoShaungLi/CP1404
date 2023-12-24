"""
CP1404/CP5632 Practical
Kivy GUI program to convert miles to kilometers
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesToKilometersApp(App):
    """MilesToKilometersApp is a  Kivy app for converting miles to kilometers"""
    output_km = StringProperty()

    def build(self):
        """Build the kivy app from kivy file"""
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_update(self):
        """Handle changes to the text input by updating the model from the view."""
        self.output_km = self.root.ids.input_miles.text

    def handle_calculation(self):
        """ handle calculation (could be button press or other call)"""
        output = self.validate_input() * MILES_TO_KM
        self.root.ids.output_label.text = str(output)
        return output

    def handle_increment(self, change):
        """Increase or decrease the number while the text is not empty."""
        if self.root.ids.input_miles.text == "":
            self.root.ids.input_miles.text = str(0)
        else:
            miles = self.validate_input() + change
            self.root.ids.input_miles.text = str(miles)

    def validate_input(self):
        """Validate input and convert to float, if invalid return 0"""
        try:
            value = float(self.root.ids.input_miles.text)
            if value < 0:
                value = 0.0
            return value
        except ValueError:
            return 0.0


MilesToKilometersApp().run()
