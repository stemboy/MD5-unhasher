import os

from appdirs import user_data_dir
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown


class EncryptionDropDown(BoxLayout):
    dropDown = DropDown()
    mainButton = Button(size_hint=(1, 1))

    def on_kv_post(self, base_widget):
        self.create()

    def create(self):
        customHashToStringFiles = [str(os.path.splitext(path)[0])
                                   for path in os.listdir(os.path.join(user_data_dir(), "md5-unhasher", "encryptions"))]

        self.dropDown.clear_widgets()
        self.remove_widget(self.mainButton)


        btn = Button(text="Community md5", size_hint_y=None, height=20)
        btn.bind(on_release=lambda _btn: self.dropDown.select(_btn.text))
        self.dropDown.add_widget(btn)

        btn = Button(text="Community sha1", size_hint_y=None, height=20)
        btn.bind(on_release=lambda _btn: self.dropDown.select(_btn.text))
        self.dropDown.add_widget(btn)

        btn = Button(text="Community sha3-256", size_hint_y=None, height=20)
        btn.bind(on_release=lambda _btn: self.dropDown.select(_btn.text))
        self.dropDown.add_widget(btn)



        for text in customHashToStringFiles:
            btn = Button(text=text, size_hint_y=None, height=20)
            btn.bind(on_release=lambda _btn: self.dropDown.select(_btn.text))

            self.dropDown.add_widget(btn)

        self.mainButton.bind(on_release=self.dropDown.open)

        self.dropDown.bind(on_select=lambda instance, x: setattr(self.mainButton, 'text', x))
        self.dropDown.select(customHashToStringFiles[0])

        self.add_widget(self.mainButton)
