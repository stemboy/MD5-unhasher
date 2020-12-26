import os

import appdirs
from kivy import Logger


def toggleButtonSelect(toggleButton):
    toggleButton.state = "down"


def emptyFunction(*args, **kwargs):
    pass


def log(*texts):
    if len(texts) == 0:
        Logger.info("")

    elif texts[0] == "\n":
        Logger.info("")
        Logger.info("")

    else:
        Logger.info("Dataset Creator: " + " ".join([str(text) for text in texts]))


def decrypt(hash, filename):
    path = os.path.join(getUsrDataDir(), "encryption_datasets", filename)


def getUsrDataDir():
    return os.path.join(appdirs.user_data_dir(), "md5-unhasher")
