from Gui.screen import Screen


class ConfigScreen(Screen):
    def on_enter(self):
        self.ids["ConfigLayout"].on_enter()
