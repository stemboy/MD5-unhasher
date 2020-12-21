import os

from kivy import Logger


def get():
    kv = ""

    for file in os.listdir("Gui/kv"):
        if file.endswith(".kv"):
            kv = kv + str(open(os.path.join("Gui", "kv", file), "r").read()) + "\n"

    Logger.info("App: Located kv files")

    return kv