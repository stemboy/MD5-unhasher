import appdirs
import os
from multiprocessing import freeze_support




if __name__ == "__main__":
    freeze_support()

    user_data_dir = str(os.path.join(appdirs.user_data_dir(), "md5-unhasher"))

    if not os.path.exists(user_data_dir):
        os.mkdir(user_data_dir)

    if not os.path.exists(os.path.join(user_data_dir, "config.ini")):
        open(os.path.join(user_data_dir, "config.ini"), "w")


    os.chdir(os.path.dirname(globals()["__file__"]))
    os.environ["KIVY_NO_ARGS"] = "1"
    os.environ["KIVY_HOME"] = str(os.path.join(user_data_dir, "kivy"))
    os.environ["KCFG_KIVY_LOG_NAME"] = "%y-%m-%d_%_.log"
    os.environ["KCFG_KIVY_LOG_DIR"] = "../logs"
    os.environ["KCFG_KIVY_LOG_LEVEL"] = "info"

    import sys
    args = sys.argv

    import kivy


    if args[-1] == "--help":
        print("Usages md5-unhasher.py [Option]",
              "                       --help               - Show this page",
              "                       --gui-only           - Run only the gui",
              "                       --array-create-only  - Run the array creator only", sep="\n")

    elif args[-1] == "--gui-only":
        from Gui import DecryptApp
        app = DecryptApp()
        app.run()

    elif args[-1] == "--array-create-only":
        from misc.array_creator import create
        create()

    else:
        print("No arguments were given or the given arguments were not correct,",
              "Usages md5-unhasher.py [Option]",
              "                       --help               - Show this page",
              "                       --gui-only           - Run only the gui",
              "                       --array-create-only  - Run the array creator only", sep="\n")
        print("Running the program as normal")

        # Nothing here, no program in place yet
