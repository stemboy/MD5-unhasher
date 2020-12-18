from kivy.uix.screenmanager import Screen


class Screen(Screen):
    def on_pre_enter(self):
        try:
            self.ids["Header"].ids[self.name + "ScreenButton"].state = "down"
        except KeyError:
            pass


