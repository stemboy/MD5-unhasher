from shutil import copyfile
import appdirs
import os
from multiprocessing import freeze_support

if __name__ == "__main__":
    freeze_support()

    user_data_dir = str(os.path.join(appdirs.user_data_dir(), "md5-unhasher"))

    if not os.path.exists(user_data_dir):
        os.mkdir(user_data_dir)

    if not os.path.exists(os.path.join(user_data_dir, "config.ini")):
        copyfile("default_config.ini", os.path.join(user_data_dir, "config.ini"))

    os.chdir(os.path.dirname(globals()["__file__"]))
    os.environ["KIVY_NO_ARGS"] = "1"
    os.environ["KIVY_HOME"] = str(os.path.join(user_data_dir, "kivy"))
    os.environ["KCFG_KIVY_LOG_NAME"] = "%y-%m-%d_%_.log"
    os.environ["KCFG_KIVY_LOG_DIR"] = "../logs"
    os.environ["KCFG_KIVY_LOG_LEVEL"] = "info"

    import sys

    args = sys.argv

    import kivy
    from kivy.logger import Logger

    Logger.info("UserDataDir: UserDataDir at \"" + str(user_data_dir) + "\"")

    Logger.info("Arguments: Program ran with the args " + str(sys.argv))

    if args[-1] == "--help":
        Logger.info("Help: \n" +
                    "Usages md5-unhasher.py [Option]\n" +
                    "                       --help               - Show this page\n" +
                    "                       --gui-only           - Run only the gui\n" +
                    "                       --array-create-only  - Run the array creator only\n")

    elif args[-1] == "--gui-only":
        Logger.info("App: Running with the gui only")

        import Gui
        from Gui import Md5_unhasher_app

        app = Md5_unhasher_app()
        app.run()

    elif args[-1] == "--array-create-only":


        Logger.info("App: Running the array creator only")

        import misc
        from misc.array_creator import create

        create()

    elif args[-1] == "--normal":


        Logger.info("App: Running the program as normal")

    else:
        Logger.warning("Arguments: No arguments were given or the given arguments were not correct,\n" +
                       "Usages md5-unhasher.py [Option]\n" +
                       "                       --help               - Show this page\n" +
                       "                       --gui-only           - Run only the gui\n" +
                       "                       --array-create-only  - Run the array creator only\n")
        Logger.info("App: Running the program as normal")

        # Nothing here, no program in place yet
