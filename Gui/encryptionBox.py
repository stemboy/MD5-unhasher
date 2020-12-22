from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown


class EncryptionBox(BoxLayout):
    buttons = ListProperty([])

    def on_kv_post(self, base_widget):
        dropdown = DropDown()

        for text in self.buttons:
            btn = Button(text=text)
            btn.bind(on_release=lambda _btn: dropdown.select(_btn.text))

            dropdown.add_widget(btn)

        mainbutton = Button(text=self.buttons[0], size_hint=(None, None))
        mainbutton.bind(on_release=dropdown.open)

        dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))

        self.add_widget(dropdown)

