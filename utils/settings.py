import json, keyboard, threading, sys
import windows.root as windowRoot

settingsFile = open("json/settings.json", "r")
obj = json.loads(settingsFile.read())

def getStartSettings():
    return obj["startButton"]

def getStopSettings():
    settingsFile = open("json/settings.json", "r")
    obj = json.loads(settingsFile.read())
    return obj["stopButton"]

def startSettings():

    windowRoot.stopClickButton.configure(state="disable")
    windowRoot.clickEntry.configure(state="disable")
    windowRoot.buttonApply.configure(state="disable")
    windowRoot.buttonStop.configure(state="disable")

    windowRoot.startClickButton.configure(text="Press any key...")
    def waitUserPress():
        key = keyboard.read_key()

        if key != obj["stopButton"]:
            obj["startButton"] = key

            writeSettingsFile = open("json/settings.json", "w")
            writeSettingsFile.write(str(obj).replace("'", '"'))
            writeSettingsFile.close()

        windowRoot.startClickButton.configure(text=obj["startButton"])

        windowRoot.stopClickButton.configure(state="normal")
        windowRoot.clickEntry.configure(state="normal")
        windowRoot.buttonApply.configure(state="normal")
        windowRoot.buttonStop.configure(state="normal")

    try:
        thread = threading.Thread(target=waitUserPress, daemon=True)
        thread.start()
    except (KeyboardInterrupt, SystemExit):
        sys.exit()

def stopSettings():

    windowRoot.startClickButton.configure(state="disable")
    windowRoot.clickEntry.configure(state="disable")
    windowRoot.buttonApply.configure(state="disable")
    windowRoot.buttonStop.configure(state="disable")

    windowRoot.stopClickButton.configure(text="Press any key...")
    def waitUserPress():
        key = keyboard.read_key()

        if key != obj["startButton"]:
            obj["stopButton"] = key

            writeSettingsFile = open("json/settings.json", "w")
            writeSettingsFile.write(str(obj).replace("'", '"'))
            writeSettingsFile.close()

        windowRoot.stopClickButton.configure(text=obj["stopButton"])

        windowRoot.startClickButton.configure(state="normal")
        windowRoot.clickEntry.configure(state="normal")
        windowRoot.buttonApply.configure(state="normal")
        windowRoot.buttonStop.configure(state="normal")

    try:
        thread = threading.Thread(target=waitUserPress, daemon=True)
        thread.start()
    except (KeyboardInterrupt, SystemExit):
        sys.exit()
