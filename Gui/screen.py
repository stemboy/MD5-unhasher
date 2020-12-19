from kivy.uix.screenmanager import Screen


class Screen(Screen):
    def on_pre_enter(self, *args, **kwargs):
        super(Screen, self).on_pre_enter(*args, **kwargs)

        try:
            self.ids["Header"].ids[self.name + "ScreenButton"].state = "down"
        except KeyError:
            pass


