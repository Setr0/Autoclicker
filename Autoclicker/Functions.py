import pyautogui, keyboard # Libraries

def autoClicking(): # Function
    import Input # Import the input (Input.py)
    while True:
        
        # Spamming clicks
        if keyboard.is_pressed('1'): # Spamming left click
            while True:
                pyautogui.click(clicks=int(Input.left_click.get())) # int is very important because we get numbers (int) not lecters (string)
                if keyboard.is_pressed('2'):
                    break
        
        elif keyboard.is_pressed('3'):  # Spamming right click
            while True:
                pyautogui.click(button = 'right', clicks=int(Input.right_click.get())) # int is very important because we get numbers (int) not lecters (string)
                if keyboard.is_pressed('4'):
                    break

        # This is for to fix a bug that when you click buttons it continues to spamm
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

        # For to change the numbers
        elif keyboard.is_pressed('5'):
            break
