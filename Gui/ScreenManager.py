from kivy import Logger
from kivy.uix.screenmanager import ScreenManager


class ScreenManager(ScreenManager):
    last_screen = None

    def nav_buttons_selected_change(self, widget, state):
        Logger.debug("App: Switching screen function | screen=\"{0}\" | state=\"{1}\"".format(widget.text, state))

        if state == "down":
            if self.last_screen != widget.text:
                Logger.info("App: Switching to screen " + widget.text)

            self.last_screen = widget.text
            
            self.current = widget.text
