import  __init__
from tkinter import CENTER
import tkinter as tk

# Window configs
window = tk.Tk()  # Window
# Icon, only .ico files, for .ico files go to: https://www.icoconverter.com/
window.iconbitmap('favicon.ico')
window.geometry('900x650+500+200')  # Window's size and position
window.title("Autoclicker")  # Window's title
window.grid_columnconfigure(0, weight=1)  # Collumn configuration
window.config(bg="#1b1b1b")  # Window's background

# The label
welcome_label = tk.Label(window, text='''Developed by Piggy 
                        \nThanks for have downloaded AutoClicker.exe
                        \n1 click = 10 CPS 
                        \nPress 1 for to start left mouse button spamming and press 2 for stop 
                        \nPress 3 for to start right mouse button spamming and press 4 for stop
                        \nPress 5 for to change the numbers''',
                         font=('Helvetica', 13),
                         fg=('white'),
                         background=('#1b1b1b'))  # Label's style

welcome_label.grid(row=0, column=0, sticky="n",
                   padx=20, pady=10)  # Label's position

ist = tk.Label(window, text='''Left clicks''',
                         font=('Helvetica', 13),
                         fg=('white'),
                         background=('#1b1b1b'))  # Label's style

ist.grid(row=1, column=0, pady=10, padx=10, sticky='w')  # Label's position

ist1 = tk.Label(window, text='''Right clicks''',
               font=('Helvetica', 13),
               fg=('white'),
               background=('#1b1b1b'))  # Label's style

ist1.grid(row=2, column=0, pady=10, padx=10, sticky = 'w')  # Label's position

# The button
button = tk.Button(text="Apply",
                   command=__init__.autoClicking,
                   background='#1b1b1b',
                   fg='white',
                   font='Helvetica')  # Button's style and command

button.grid(row=3, column=0, sticky="WE",
            padx=50, pady=20)  # Button's position

import __input__

if __name__ == "__main__":
    window.mainloop()  # Window's mainloop

