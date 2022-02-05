from tkinter import * 
import pyautogui, keyboard, subprocess

window = Tk()
window.geometry("900x650+530+200")
window.title("Autoclicker")
window.resizable(False, False)
window.config(bg='#1b1b1b')
window.iconbitmap('favicon.ico')

titleApp = Label(window, text='Autoclicker', font=('Helvetica', 30), fg=('white'), background=('#1b1b1b'))
titleApp.place(x=350, y=30)

istrunctions = Label(window, text='''1 click = 10 CPS 
                        \nPress 1 for to start left mouse button spamming and press 2 for stop 
                        \nPress 3 for to start right mouse button spamming and press 4 for stop''',
                         font=('Helvetica', 15),
                         fg=('white'),
                         background=('#1b1b1b'))  
istrunctions.place(x=140, y=100)

leftClicks = Label(window, text='''Left clicks''', font=('Helvetica', 15), fg=('white'), background=('#1b1b1b'))  
leftClicks.place(x=50, y=300)

rightClicks = Label(window, text='''Right clicks''', font=('Helvetica', 15), fg=('white'), background=('#1b1b1b'))  
rightClicks.place(x=50, y=400)

def autoClicking():
    window.state("withdrawn")
    subprocess.Popen(['pythonw', 'notify.pyw'])

    while True:
        if keyboard.is_pressed('1'):
            while True:
                pyautogui.click(clicks=int(left_click.get()))
                if keyboard.is_pressed('2'):
                    break

        elif keyboard.is_pressed('3'):  
            while True:
                pyautogui.click(button='right', clicks=int(
                    right_click.get()))
                if keyboard.is_pressed('4'):
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

        elif keyboard.is_pressed('5'):
            window.deiconify()  
            break

buttonApply = Button(text="Apply", command=autoClicking, background='#1b1b1b', fg='white', font='Helvetica', activebackground='#292929')
buttonApply.place(x=380, y=480, width=100, height=50)

infoLabel = Label(window, text='''Press 5 for to change the numbers''', font=('Helvetica', 24), fg=('white'), background=('#1b1b1b'))
infoLabel.place(x=170, y=570)

left_click = Entry(background='#1b1b1b', fg='white', font='Helvetica', insertbackground='white')
left_click.place(x=200, y=300, width=500, height=30)

right_click = Entry(background='#1b1b1b', fg='white', font='Helvetica', insertbackground='white')
right_click.place(x=200, y=400, width=500, height=30)

window.mainloop()  