from kivy.properties import OptionProperty, StringProperty, ObjectProperty, NumericProperty, Logger
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.slider import Slider
from kivy.uix.textinput import TextInput

from misc.config import config


class ConfigItem(FloatLayout):
    type = OptionProperty("string", options=["slider", "numeric", "string", "bool"])
    title = StringProperty("Title")
    description = StringProperty("Description")
    min = NumericProperty(None)
    max = NumericProperty(None)
    sliderMin = NumericProperty(None)
    sliderMax = NumericProperty(None)
    section = StringProperty("")
    key = StringProperty("")

    _editorHolder = ObjectProperty()
    _editorWidget = ObjectProperty()
    _editorWidget2 = ObjectProperty(None)

    def on_kv_post(self, base_widget):
        self._editorHolder = self.ids["EditorHolder"]

        self.bind(type=self.update,
                  title=self.update,
                  description=self.update,
                  min=self.update,
                  max=self.update)

        self.update()

    def text_box_validator(self, *args):
        numb = int(self._editorWidget2.text)

        if self.min is not None and numb < self.min:
            numb = self.min

        elif self.max is not None and numb < self.max:
            numb = self.max

        self._editorWidget2.text = str(numb)
        self.value_changed(None, numb)

    def update(self, *args):
        self.ids["Title"].text = self.title
        self.ids["Description"].text = self.description

        self._editorHolder.clear_widgets()

        if self.type == "slider":
            if self.sliderMin is None or self.sliderMax is None:
                raise ValueError("'sliderMin' and / or 'sliderMax' cannot be 'None' if type is slider")

            self._editorWidget = Slider(min=self.sliderMin, max=self.sliderMax,
                                        value=config.getint(self.section, self.key), step=1)
            self._editorWidget.bind(value=self.value_changed)

            self._editorWidget2 = TextInput(multiline=False, font_size=self._editorHolder.height/2,
                                            text=config.get(self.section, self.key), input_filter="int")
            self._editorWidget2.bind(on_text_validate=self.text_box_validator)
            self._editorWidget2.bind(focus=self.text_box_validator)


        if self._editorWidget2 is not None:
            self._editorHolder.add_widget(self._editorWidget2)

        self._editorHolder.add_widget(self._editorWidget)

    def value_changed(self, _, value):
        if self._editorWidget2 is not None:
            self._editorWidget2.text = str(value)

            self._editorWidget.value = int(value)


        Logger.info("Config: " + self.section + self.key + " set to " + str(value))
        config.set(self.section, self.key, value)
        config.write()
        Logger.info("Config: Saved config")
