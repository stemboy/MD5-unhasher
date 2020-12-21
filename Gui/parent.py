from kivy import Logger
from kivy.uix.gridlayout import GridLayout


class Parent(GridLayout):
    last_screen = None

    def on_parent(self, *args):
        self.ids["Nav"].ids["HomeScreenButton"].state = "down"

    def nav_buttons_selected_change(self, widget, state):
        Logger.debug("App: Switching screen function | screen=\"{0}\" | state=\"{1}\"".format(widget.text, state))

        if state == "down":
            if self.last_screen != widget.text:
                Logger.info("App: Switching to screen " + widget.text)

            self.last_screen = widget.text

            self.ids["ScreenManager"].current = widget.text
