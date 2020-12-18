from kivy.uix.screenmanager import ScreenManager


class ScreenManager(ScreenManager):
    def header_buttons_selected_change(self, widget, state):
        if state == "down":
            self.current = widget.text
