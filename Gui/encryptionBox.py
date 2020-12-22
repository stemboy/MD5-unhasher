from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown


class EncryptionBox(BoxLayout):
    buttons = ListProperty([])
    dropDown = DropDown()
    mainButton = Button(size_hint=(1, 1))

    def on_kv_post(self, base_widget):
        for text in self.buttons:
            btn = Button(text=text, size_hint_y=None, height=20)
            btn.bind(on_release=lambda _btn: self.dropDown.select(_btn.text))

            self.dropDown.add_widget(btn)

        self.mainButton.text = self.buttons[0]
        self.mainButton.bind(on_release=self.dropDown.open)

        self.dropDown.bind(on_select=lambda instance, x: setattr(self.mainButton, 'text', x))

        self.add_widget(self.mainButton)

