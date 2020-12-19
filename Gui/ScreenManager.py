from kivy.uix.screenmanager import ScreenManager


class ScreenManager(ScreenManager):
    def nav_buttons_selected_change(self, widget, state):
        if state == "down":
            self.current = widget.text
