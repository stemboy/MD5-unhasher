from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

Decrypted = ("Testcles")
Form = ("MD5")


class HashDecrypter(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 2

        self.add_widget(Label(text="Input hash:"))

        self.todecrypt = TextInput(multiline=False)
        self.add_widget(self.todecrypt)

        self.add_widget(Label(text="Text found:"))
        self.add_widget(Label(text=Decrypted))


class DecryptApp(App):
    def build(self):
        return HashDecrypter()


if __name__ == "__main__":
    DecryptApp().run()
