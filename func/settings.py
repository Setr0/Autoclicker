import json, keyboard, threading, sys
from windows.root import startClickButton, stopClickButton, clickEntry, buttonApply, buttonStop

settingsFile = open("json/settings.json", "r")
obj = json.loads(settingsFile.read())

def getStartSettings():
    return obj["startButton"]

def getStopSettings():
    settingsFile = open("json/settings.json", "r")
    obj = json.loads(settingsFile.read())
    return obj["stopButton"]

def startSettings():

    stopClickButton.config(state="disable")
    clickEntry.config(state="disable")
    buttonApply.config(state="disable")
    buttonStop.config(state="disable")

    startClickButton.config(text="Press any key...")
    def waitUserPress():
        key = keyboard.read_key()

        if key != obj["stopButton"]:
            obj["startButton"] = key

            writeSettingsFile = open("json/settings.json", "w")
            writeSettingsFile.write(str(obj).replace("'", '"'))
            writeSettingsFile.close()

        startClickButton.config(text=obj["startButton"])
        
        stopClickButton.config(state="normal")
        clickEntry.config(state="normal")
        buttonApply.config(state="normal")
        buttonStop.config(state="normal")

    try:
        thread = threading.Thread(target=waitUserPress, daemon=True)
        thread.start()
    except (KeyboardInterrupt, SystemExit):
        sys.exit()

def stopSettings():

    startClickButton.config(state="disable")
    clickEntry.config(state="disable")
    buttonApply.config(state="disable")
    buttonStop.config(state="disable")

    stopClickButton.config(text="Press any key...")
    def waitUserPress():
        key = keyboard.read_key()

        if key != obj["startButton"]:
            obj["stopButton"] = key

            writeSettingsFile = open("json/settings.json", "w")
            writeSettingsFile.write(str(obj).replace("'", '"'))
            writeSettingsFile.close()

        stopClickButton.config(text=obj["stopButton"])
        
        startClickButton.config(state="normal")
        clickEntry.config(state="normal")
        buttonApply.config(state="normal")
        buttonStop.config(state="normal")

    try:
        thread = threading.Thread(target=waitUserPress, daemon=True)
        thread.start()
    except (KeyboardInterrupt, SystemExit):
        sys.exit()