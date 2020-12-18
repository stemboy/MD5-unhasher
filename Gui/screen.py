from kivy.uix.screenmanager import Screen


class Screen(Screen):
    def on_pre_enter(self):
        print(1)
        try:
            print(22, self.name + "ScreenButton", self.ids)
            self.ids["Header"].ids[self.name + "ScreenButton"].state = "down"
        except KeyError:
            print(22, self.name + "ScreenButton", self.ids)
        print()

