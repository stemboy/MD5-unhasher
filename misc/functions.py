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
