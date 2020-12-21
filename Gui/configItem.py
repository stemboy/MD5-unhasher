from kivy.properties import OptionProperty, StringProperty, ObjectProperty, NumericProperty, Logger
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.slider import Slider

from misc.config import config


class ConfigItem(FloatLayout):
    type = OptionProperty("string", options=["slider", "numeric", "string", "bool"])
    title = StringProperty("Title")
    description = StringProperty("Description")
    min = NumericProperty(None)
    max = NumericProperty(None)
    section = StringProperty("")
    key = StringProperty("")

    _editorHolder = ObjectProperty()
    _editorWidget = ObjectProperty()

    def on_kv_post(self, base_widget):
        self._editorHolder = self.ids["EditorHolder"]

        self.bind(type=self.update,
                  title=self.update,
                  description=self.update,
                  min=self.update,
                  max=self.update)

        self.update()

    def update(self, *args):
        self.ids["Title"].text = self.title
        self.ids["Description"].text = self.description

        self._editorHolder.clear_widgets()

        if self.type == "slider":
            if self.min is None or self.max is None:
                raise ValueError("'min' and / or 'max' cannot be 'None' if type is slider")

            self._editorWidget = Slider(min=self.min, max=self.max, value=config.getint(self.section, self.key), step=1)
            self._editorWidget.bind(value=self.value_changed)

        self._editorHolder.add_widget(self._editorWidget)

    def value_changed(self, _, value):
        Logger.info("Config: " + self.section + self.key + " set to " + str(value))
        config.set(self.section, self.key, value)
        config.write()
        Logger.info("Config: Saved")
