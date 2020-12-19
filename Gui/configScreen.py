from kivy.config import ConfigParser

from Gui.screen import Screen


class ConfigScreen(Screen):
    config = ConfigParser()

    def __init__(self, *args, **kwargs):
        super(ConfigScreen, self).__init__(*args, **kwargs)


    def on_kv_post(self, *args):
        self.ids["ConfigPanel"].add_json_panel('String Content',
                                               self.config, 'Gui/config_markdown/string_content.json')
        self.ids["ConfigPanel"].add_json_panel('String Character Types',
                                               self.config, 'Gui/config_markdown/string_character_types.json')
        self.ids["ConfigPanel"].add_json_panel('String Creation',
                                               self.config, 'Gui/config_markdown/string_creation.json')
        self.ids["ConfigPanel"].add_json_panel('Development',
                                               self.config, 'Gui/config_markdown/development.json')
