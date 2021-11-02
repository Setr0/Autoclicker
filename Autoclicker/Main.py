12
import Functions
from tkinter import CENTER
import tkinter as tk

from window import window # The window

# The label
label = tk.Label(window, text='''Developed by Piggy 
                        \nThanks for have downloaded AutoClicker.exe
                        \n1 click = 10 CPS 
                        \nPress 1 for to start left mouse button spamming and press 2 for stop 
                        \nPress 3 for to start right mouse button spamming and press 4 for stop''',
                         font=('Helvetica', 15),
                         fg=('white'),
                         background=('#1b1b1b'))  # Label's style

label.grid(row=0, column=0, sticky="n",
                   padx=20, pady=10)  # Label's position

change = tk.Label(window, text='''Press 5 for to change the numbers''',
                         font=('Helvetica', 24),
                         fg=('red'),
                         background=('#1b1b1b'))  # Label's style

change.grid(row=4, column=0,
                   padx=20, pady=70, sticky="s")  # Label's position

ist = tk.Label(window, text='''Left clicks''',
                         font=('Helvetica', 15),
                         fg=('white'),
                         background=('#1b1b1b'))  # Label's style

ist.grid(row=1, column=0, pady=10, padx=10, sticky='w')  # Label's position


ist1 = tk.Label(window, text='''Right clicks''',
               font=('Helvetica', 15),
               fg=('white'),
               background=('#1b1b1b'))  # Label's style

ist1.grid(row=2, column=0, pady=10, padx=10, sticky = 'w')  # Label's position

# The button
button = tk.Button(text="Apply",
                   command=Functions.autoClicking,
                   background='#1b1b1b',
                   fg='white',
                   font='Helvetica')  # Button's style and command

button.grid(row=3, column=0, sticky="WE",
            padx=50, pady=20)  # Button's position


import Input # Importing the input

if __name__ == "__main__":
    window.mainloop()  # Window's mainloop

