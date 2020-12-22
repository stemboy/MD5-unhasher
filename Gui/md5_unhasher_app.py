from kivy import Logger
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import BooleanProperty
from kivy.metrics import cm

from Gui import kv
from Gui.ScreenManager import ScreenManager
from Gui.homeScreen import HomeScreen
from Gui.hashingScreen import HashingScreen
from Gui.decryptScreen import DecryptScreen
from Gui.configScreen import ConfigScreen
from Gui.configLayout import ConfigLayout
from Gui.configItem import ConfigItem
from Gui.encryptionDropDown import EncryptionDropDown
from Gui.parent import Parent


class Md5_unhasher_app(App):
    gui_only = BooleanProperty(False)

    def build(self):
        Logger.info("App: Started build")
        for kvFilePath in kv.get():
            Builder.load_file(kvFilePath)
        Logger.info("App: Built kv")

        Window.size = cm(23), cm(18)
        Window.minimum_width, Window.minimum_height = cm(23), cm(18)
        Window.bind(size=print)
        Logger.info("App: Set window size and minimum size")

        return Parent()
