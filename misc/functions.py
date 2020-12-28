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


def log_warning(*texts):
    if len(texts) == 0:
        Logger.warning("")

    elif texts[0] == "\n":
        Logger.warning("")
        Logger.warning("")

    else:
        Logger.warning("Dataset Creator: " + " ".join([str(text) for text in texts]))

def log_critical(*texts):
    if len(texts) == 0:
        Logger.critical("")

    elif texts[0] == "\n":
        Logger.critical("")
        Logger.critical("")

    else:
        Logger.critical("Dataset Creator: " + " ".join([str(text) for text in texts]))


def decrypt(hash, filename):
    path = os.path.join(getUsrDataDir(), "encryption_datasets", filename)


def getUsrDataDir():
    return os.path.join(appdirs.user_data_dir(), "md5-unhasher")
