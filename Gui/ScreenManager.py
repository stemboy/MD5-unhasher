from kivy.uix.screenmanager import ScreenManager


class ScreenManager(ScreenManager):
    def header_buttons_selected_change(self, widget, value):
        if value == "down":
            self.current = widget.text
