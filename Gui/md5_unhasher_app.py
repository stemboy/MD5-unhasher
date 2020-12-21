from kivy import Logger
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder

from Gui import kv
from Gui.ScreenManager import ScreenManager
from Gui.homeScreen import HomeScreen
from Gui.hashingScreen import HashingScreen
from Gui.decryptScreen import DecryptScreen
from Gui.configScreen import ConfigScreen
from Gui.configLayout import ConfigLayout
from Gui.configItem import ConfigItem


class Md5_unhasher_app(App):
    def build(self):
        Logger.info("App: Started build")
        Builder.load_string(kv.get())
        Logger.info("App: Built kv")

        Window.minimum_width, Window.minimum_height = "25cm", " 25cm"
        Window.size = Window.minimum_width, Window.minimum_height
        Logger.info("App: Set window size and minimum size")

        return ScreenManager()