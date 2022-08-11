import pyautogui, keyboard, win10toast, threading
from windows.root import END, clickEntry, buttonApply, stopClickButton, startClickButton
from func.settings import obj

global running
running = False

def autoClicking():
    toaster = win10toast.ToastNotifier()
    toaster.show_toast("Autoclicker", "Click STOP for changing the numbers", icon_path="icon/favicon.ico", threaded=True)
    while running:
        if keyboard.read_key() == obj["startButton"]:
            while True:
                pyautogui.click(clicks=int(clickEntry.get()))
                if keyboard.is_pressed(obj["stopButton"]):
                    break
                if not running:
                    break

def stop():
    clickEntry.config(state="normal")
    buttonApply.config(state="normal")
    stopClickButton.config(state="normal")
    startClickButton.config(state="normal")
    global running
    if running:
        running = False

def run():
    try :
        if int(clickEntry.get()):
            global running
            if not running:
                clickEntry.config(state="disabled")
                buttonApply.config(state="disabled")
                stopClickButton.config(state="disabled")
                startClickButton.config(state="disabled")
                running = True
                thread = threading.Thread(target=autoClicking)
                thread.start()
    except:
        clickEntry.delete(0, END)
        clickEntry.insert(0, "Only numbers")

