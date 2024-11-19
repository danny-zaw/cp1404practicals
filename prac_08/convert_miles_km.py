"""


"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

MILES_TO_KM_CONVERSION = 1.60934

class ConvertMilesToKmApp(App):
    output_text = StringProperty("0.0")

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (400, 200)
        self.title = "Convert Miles to Km"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_miles_to_km(self):
        """Convert miles to kilometers and update the label."""
        try:
            miles = float(self.root.ids.input_number.text)
            kilometers = miles * MILES_TO_KM_CONVERSION
            self.output_text = f"{kilometers}"
        except ValueError:
            self.output_text = "0.0"

    def handle_increment(self, change):
        """Increase or decrease text input by 1."""
        try:
            current_value = int(self.root.ids.input_number.text)
        except ValueError:
            current_value = 0
        self.root.ids.input_number.text = str(current_value + change)

ConvertMilesToKmApp().run()

