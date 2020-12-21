import os

from kivy import Logger


def get():
    kvPaths = list()

    kvPaths.append(os.path.join("Gui", "kv", "imports.kv"))

    for fileName in os.listdir("Gui/kv"):
        if fileName.endswith(".kv") and fileName != "imports.kv":
            kvPaths.append(os.path.join("Gui", "kv", fileName))


    Logger.info("App: Located kv files")
    Logger.debug("App: Kv paths are {}".format(kvPaths))

    return kvPaths
