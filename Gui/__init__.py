from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder


from Gui.ScreenManager import ScreenManager
from Gui.homeScreen import HomeScreen
from Gui.hashingScreen import HashingScreen
from Gui.decryptScreen import DecryptScreen
from Gui.configScreen import ConfigScreen


class DecryptApp(App):
    def build(self):
        Builder.load_file('Gui/widgets.kv')
        Builder.load_file('Gui/screens.kv')
        Window.minimum_width, Window.minimum_height = "25cm", " 25cm"
        Window.size = Window.minimum_width, Window.minimum_height
        return ScreenManager()


if __name__ == "__main__":
    import os
    os.chdir(os.path.split(os.path.dirname(globals()["__file__"]))[0])

    DecryptApp().run()
