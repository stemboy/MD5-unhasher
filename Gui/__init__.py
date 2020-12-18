from kivy.app import App
from kivy.lang import Builder

from Gui.ScreenManager import ScreenManager
from Gui.homeScreen import HomeScreen
from Gui.hashingScreen import HashingScreen


class DecryptApp(App):
    def build(self):
        return ScreenManager()


if __name__ == "__main__":
    Builder.load_file('kv.kv')
    DecryptApp().run()
