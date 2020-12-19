from kivy.config import ConfigParser
from kivy.uix.settings import Settings

from Gui.screen import Screen


class ConfigScreen(Screen):
    config = ConfigParser()

    def __init__(self, *args, **kwargs):
        super(ConfigScreen, self).__init__(*args, **kwargs)


    def on_kv_post(self, *args):
        self.ids["ConfigPannel"].add_json_panel('My custom panel', self.config, 'Gui/config_markdown/con1.json')
