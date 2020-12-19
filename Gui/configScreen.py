import os

import appdirs
from kivy.config import ConfigParser

from Gui.screen import Screen


class ConfigScreen(Screen):
    def on_kv_post(self, *args, **kwargs):
        super(ConfigScreen, self).on_kv_post(*args, **kwargs)

        self.config = ConfigParser()
        self.config.read(os.path.join(appdirs.user_data_dir(), "md5-unhasher", "config.ini"))

        self.ids["ConfigPanel"].add_json_panel('String Content',
                                               self.config, 'Gui/config_markdown/string_content.json')
        self.ids["ConfigPanel"].add_json_panel('Hash and String Creation',
                                               self.config, 'Gui/config_markdown/string_creation.json')
        self.ids["ConfigPanel"].add_json_panel('Development',
                                               self.config, 'Gui/config_markdown/development.json')
