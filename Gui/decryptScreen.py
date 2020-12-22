from kivy import Logger

from Gui.screen import Screen


class DecryptScreen(Screen):
    def decrypt(self):
        string = self.ids["DecryptedText"].text
        dataset = self.ids["EncryptionType"].mainButton.text

        Logger.info("App: Decrypting " + string + " using " + dataset + "dataset")
