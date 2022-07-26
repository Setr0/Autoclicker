import pyautogui, keyboard, win10toast, threading
from window import END, clickEntry

global running
running = False

def autoClicking():
    toaster = win10toast.ToastNotifier()
    toaster.show_toast("Autoclicker", "Click STOP for changing the numbers", icon_path="favicon.ico", threaded=True)
    while running:
        if keyboard.read_key() == '1':
            while True:
                pyautogui.click(clicks=int(clickEntry.get()))
                if keyboard.is_pressed('2'):
                    break
                if not running:
                    break

def stop():
    global running
    if running:
        running = False

def run():
    try :
        if int(clickEntry.get()):
            global running
            if not running:
                running = True
                thread = threading.Thread(target=autoClicking)
                thread.start()
    except:
        clickEntry.delete(0, END)
        clickEntry.insert(0, "Only numbers")

