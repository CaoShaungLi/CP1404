from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelApp(App):
    """DynamicLabelApp is a Kivy App to display list of names."""

    def __init__(self):
        """Construct main app"""
        super().__init__()
        self.names = ["Bob", "Cindy", "Lin", "Troy"]

    def build(self):
        """Build the Kivy GUI"""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicLabelApp().run()
