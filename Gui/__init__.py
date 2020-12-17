from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


class ScreenManager(ScreenManager):
    pass


class Screen1(Screen):
    pass


class DecryptApp(App):
    def build(self):
        return ScreenManager()


if __name__ == "__main__":
    Builder.load_file('kv.kv')
    DecryptApp().run()
