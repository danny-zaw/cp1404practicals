"""
CP1404 - Practical 8
Program: Dynamic Labels (kivy app)
Estimated: 1 hour
Actual: 30 minutes
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # basic data (model) - list of names
        self.names = {"Danny", "Bryan", "Jason", "Sophia"}

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')

        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)

        return self.root

DynamicLabelsApp().run()