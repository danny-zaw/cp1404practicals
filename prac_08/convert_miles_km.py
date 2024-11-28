"""
CP1404 - Practical 8
Program: Convert Miles to Km (Kivy App)
Estimated: 1 hour
Actual: 1 hour 20 minutes
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

MILES_TO_KM_CONVERSION = 1.60934

class ConvertMilesToKmApp(App):
    output_km = StringProperty("0.0")

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (400, 200)
        self.title = "Convert Miles to Km"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_conversion(self):
        """Convert miles to kilometers and update the label."""
        try:
            miles = float(self.root.ids.input_miles.text)
            kilometers = miles * MILES_TO_KM_CONVERSION
            self.output_km = f"{kilometers}"
        except ValueError:
            self.output_km = "0.0"

    def handle_increment(self, change):
        """Increase or decrease text input by 1."""
        try:
            miles = int(self.root.ids.input_miles.text)
        except ValueError:
            miles = 0
        self.root.ids.input_miles.text = str(miles + change)

ConvertMilesToKmApp().run()

