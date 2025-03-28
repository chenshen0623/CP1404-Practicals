from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesConvert(App):
    """ MilesConverter is a Kivy App for converting miles to kilometres."""
    converted_distance = StringProperty()

    def build(self):
        """ Build the Kivy app from the kv file."""
        self.title = 'Miles Converter'
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculation(self):
        """Handle calculation (could be button press or other call)."""
        value = self.get_valid_miles()
        self.converted_distance = str(value * MILES_TO_KM)
