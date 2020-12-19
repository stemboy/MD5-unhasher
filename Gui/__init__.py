from Gui.md5_unhasher_app import Md5_unhasher_app
from Gui import *

if __name__ == "__main__":
    import os
    os.chdir(os.path.split(os.path.dirname(globals()["__file__"]))[0])

    Md5_unhasher_app().run()
