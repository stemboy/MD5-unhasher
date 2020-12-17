import kivy
kivy.require('2.0.0')

run = True

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class MainScreen(GridLayout):

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='Enter text to decrypt:'))
        self.ToDecrypt = TextInput(multiline=False)
        self.add_widget(self.ToDecrypt)




class DeCryptApp(App):

    def build(self):
        return MainScreen()

if run == True:
    DeCryptApp().run()