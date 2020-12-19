import os

import appdirs
from kivy.config import ConfigParser


config = ConfigParser()
config.read(os.path.join(appdirs.user_data_dir(), "md5-unhasher", "config.ini"))
config.set("string_character_types", "space", " ")

__all__ = ["config"]
