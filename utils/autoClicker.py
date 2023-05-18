import pyautogui, keyboard, win10toast, threading
from windows.root import END, clickEntry, buttonApply, stopClickButton, startClickButton
from utils.settings import obj

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
    clickEntry.configure(state="normal")
    buttonApply.configure(state="normal")
    stopClickButton.configure(state="normal")
    startClickButton.configure(state="normal")

    global running
    if running:
        running = False

def run():
    try:
        if not int(clickEntry.get()): return

        global running
        if not running:
            clickEntry.configure(state="disabled")
            buttonApply.configure(state="disabled")

            stopClickButton.configure(state="disabled")

            startClickButton.configure(state="disabled")

            running = True
            thread = threading.Thread(target=autoClicking, daemon=True)
            thread.start()
            
    except:
        clickEntry.delete(0, END)
        clickEntry.insert(0, "Only numbers")
