from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """BoxLayoutDemo is a Kivy app for prompt username and greet them"""
    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Handle greet when button press, greet user from text input"""
        # print('greet')
        # print("test")
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """Handle clear when button press, clear text input"""
        self.root.ids.output_label.text = " "


BoxLayoutDemo().run()
