from kivy.uix.settings import *

from Gui.screen import Screen
from misc.config import config


class ConfigScreen(Screen):
    config = config

    def __init__(self, *args, **kwargs):
        super(ConfigScreen, self).__init__(*args, **kwargs)

        self.settings = SettingsWithTabbedPanel()
        self.settings.id = "ConfigPanel"
        self.settings.pos_hint = {"y": 0}
        self.settings.size_hint = (1, 0.9)

        self.settings.add_json_panel('Custom Mining',
                                     self.config, 'Gui/config_markdown/string_content.json')
        self.settings.add_json_panel('Mining',
                                     self.config, 'Gui/config_markdown/string_creation.json')
        self.settings.add_json_panel('Development',
                                     self.config, 'Gui/config_markdown/development.json')

        self.add_widget(self.settings)



