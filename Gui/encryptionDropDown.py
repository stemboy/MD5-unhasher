import os

from appdirs import user_data_dir
from kivy import Logger
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown

from misc.functions import getUsrDataDir


class EncryptionDropDown(BoxLayout):
    dropDown = DropDown()
    mainButton = Button(size_hint=(1, 1))

    def on_kv_post(self, base_widget):
        self.create()

    def create(self):
        self.dropDown.clear_widgets()
        self.remove_widget(self.mainButton)


        md5Btn = Button(text="Community md5", size_hint_y=None, height=20)
        md5Btn.bind(on_release=lambda _btn: self.dropDown.select(_btn.text))
        self.dropDown.add_widget(md5Btn)

        sha1Btn = Button(text="Community sha1", size_hint_y=None, height=20)
        sha1Btn.bind(on_release=lambda _btn: self.dropDown.select(_btn.text))
        self.dropDown.add_widget(sha1Btn)

        sha3_256Btn = Button(text="Community sha3-256", size_hint_y=None, height=20)
        sha3_256Btn.bind(on_release=lambda _btn: self.dropDown.select(_btn.text))
        self.dropDown.add_widget(sha3_256Btn)

        if App.get_running_app().gui_only:
            Logger.warning("Encryption DropDown: Failed to load custom encryption files as app run with --gui-only arg")

        else:
            customHashToStringFiles = [str(os.path.splitext(path)[0])
                                       for path in os.listdir(os.path.join(getUsrDataDir(), "encryption_datasets"))]
            Logger.debug("Encryption DropDown: Loaded custom encryption files")

            for text in customHashToStringFiles:
                btn = Button(text=text, size_hint_y=None, height=20)
                btn.bind(on_release=lambda _btn: self.dropDown.select(_btn.text))

                self.dropDown.add_widget(btn)

        self.mainButton.bind(on_release=self.dropDown.open)

        self.dropDown.bind(on_select=lambda instance, x: setattr(self.mainButton, 'text', x))
        self.dropDown.select(md5Btn.text)

        self.add_widget(self.mainButton)
