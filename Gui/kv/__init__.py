import os

from kivy import Logger


def get():
    kv = ""

    with open(os.path.join("Gui", "kv", "imports.kv"), "r") as file:
        kv = kv + str(file.read()) + "\n\n\n"

    for fileName in os.listdir("Gui/kv"):
        if fileName.endswith(".kv") and fileName != "imports.kv":
            with open(os.path.join("Gui", "kv", fileName), "r") as file:
                kv = kv + "\n" + str(file.read()) + "\n\n"


    Logger.info("App: Located kv files")

    return kv
