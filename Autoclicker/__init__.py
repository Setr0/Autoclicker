import pyautogui, keyboard

def autoClicking():
    import __input__
    while True:
        if keyboard.is_pressed('1'):
            while True:
                pyautogui.click(clicks=int(__input__.click_sinistro.get()))
                if keyboard.is_pressed('2'):
                    break
        
        elif keyboard.is_pressed('3'):
            while True:
                pyautogui.click(button = 'right', clicks=int(__input__.click_destro.get()))
                if keyboard.is_pressed('4'):
                    break

        elif keyboard.is_pressed('5'):
            break

        elif keyboard.is_pressed('w'):
            print(' ')
        elif keyboard.is_pressed('a'):
            print(' ')
        elif keyboard.is_pressed('s'):
            print(' ')
        elif keyboard.is_pressed('d'):
            print(' ')
        elif keyboard.is_pressed('space'):
            print(' ')

# def noAutoClicking():
#     if keyboard.is_pressed('w'):
#         print(' ')
#     if keyboard.is_pressed('a'):
#         print(' ')
#     if keyboard.is_pressed('s'):
#         print(' ')
#     if keyboard.is_pressed('d'):
#         print(' ')
#     if keyboard.is_pressed('space'):
#         print(' ')
