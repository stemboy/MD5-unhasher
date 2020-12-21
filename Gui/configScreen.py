from Gui.screen import Screen


class ConfigScreen(Screen):
    has_entered_already = False

    def on_enter(self):
        if not self.has_entered_already:
            self.ids["ConfigLayout"].on_enter()
            self.has_entered_already = True
