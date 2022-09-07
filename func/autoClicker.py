import pyautogui, keyboard, win10toast, threading
from windows.root import END, clickEntry, buttonApply, stopClickButton, startClickButton
from func.settings import obj
from func.widgetsFunctions import *

global running
running = False

def autoClicking():
    toaster = win10toast.ToastNotifier()
    toaster.show_toast("Autoclicker", "Click STOP for changing the numbers", icon_path="icon/favicon.ico", threaded=True)
    while running:
        if keyboard.read_key() == obj["startButton"]:
            while True:
                if int(clickEntry.get()) >= 10:
                    pyautogui.PAUSE = 0.1
                    pyautogui.click(clicks=int(clickEntry.get()) // 10)
                else:
                    pyautogui.PAUSE = 0.8 / int(clickEntry.get())
                    pyautogui.click()

                if keyboard.is_pressed(obj["stopButton"]):
                    break
                if not running:
                    break

def stop():
    clickEntry.config(state="normal")

    buttonApply.config(state="normal")
    buttonApply.bind("<Enter>", hoverOnApply)
    buttonApply.bind("<Leave>", hoverOffApply)

    stopClickButton.config(state="normal")
    stopClickButton.bind("<Enter>", hoverOnStopClick)
    stopClickButton.bind("<Leave>", hoverOffStopClick)

    startClickButton.config(state="normal")
    startClickButton.bind("<Enter>", hoverOnStartClick)
    startClickButton.bind("<Leave>", hoverOffStartClick)

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
                buttonApply.unbind("<Enter>")

                stopClickButton.config(state="disabled")
                stopClickButton.unbind("<Enter>")
                
                startClickButton.config(state="disabled")
                startClickButton.unbind("<Enter>")

                running = True
                thread = threading.Thread(target=autoClicking, daemon=True)
                thread.start()
    except:
        clickEntry.delete(0, END)
        clickEntry.insert(0, "Only numbers")

