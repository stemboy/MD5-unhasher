import sys
import os

os.chdir(os.path.dirname(globals()["__file__"]))
os.environ["KIVY_NO_ARGS"] = "1"

from Gui import DecryptApp
from misc.array_creator import create

args = sys.argv

if args[-1] == "--help":
    print("Usages MD5-unhasher.py [Option]",
          "                       --help               - Show this page",
          "                       --gui-only           - Run only the gui",
          "                       --array-create-only  - Run the array creator only", sep="\n")

elif args[-1] == "--gui-only":
    app = DecryptApp()
    app.run()

elif args[-1] == "--array-create-only":
    create()

else:
    print("No arguments were given or the given arguments were not correct,",
          "Usages MD5-unhasher.py [Option]",
          "                       --help               - Show this page",
          "                       --gui-only           - Run only the gui",
          "                       --array-create-only  - Run the array creator only", sep="\n")
    print("Running the program as normal")

    # Nothing here, no program in place yet
