import json, keyboard
from windows.root import startClickButton, stopClickButton

settingsFile = open("json/settings.json", "r")
obj = json.loads(settingsFile.read())

def getStartSettings():
    return obj["startButton"]

def getStopSettings():
    settingsFile = open("json/settings.json", "r")
    obj = json.loads(settingsFile.read())
    return obj["stopButton"]

def startSettings():
    key = keyboard.read_key()
    obj["startButton"] = key

    writeSettingsFile = open("json/settings.json", "w")
    writeSettingsFile.write(str(obj).replace("'", '"'))
    writeSettingsFile.close()

    startClickButton.config(text=obj["startButton"])

def stopSettings():
    key = keyboard.read_key()
    obj["stopButton"] = key

    writeSettingsFile = open("json/settings.json", "w")
    writeSettingsFile.write(str(obj).replace("'", '"'))
    writeSettingsFile.close()

    stopClickButton.config(text=obj["stopButton"])