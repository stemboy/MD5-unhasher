import os

import appdirs
from kivy.config import ConfigParser as Cp


class ConfigParser(Cp):
    def get(self, *args, **kwargs):
        value = super(ConfigParser, self).get(*args, **kwargs)

        if value.startswith("[s]"):
            return str(value).replace("[s]", "")

        elif value.startswith("[i]"):
            return int(str(value).replace("[i]", ""))

        elif value.startswith("[b]"):
            if value == "True":
                return True
            elif value == "False":
                return False
            else:
                print("wtf, configparser wiered lol what")

        else:
            try:
                return int(value)

            except ValueError:
                try:
                    return float(value)

                except ValueError:
                    if value == "True":
                        return True
                    elif value == "False":
                        return False
                    else:
                        return str(value)


config = ConfigParser()
config.read(os.path.join(appdirs.user_data_dir(), "md5-unhasher", "config.ini"))
config.set("string_character_types", "space", " ")

__all__ = ["config"]
