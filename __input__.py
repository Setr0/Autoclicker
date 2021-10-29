import tkinter as tk
from typing import Text  # Import the tkinter library

# Making the text input
click_sinistro = tk.Entry()

# Text input's position
click_sinistro.grid(row=1, column=0, sticky="WE", padx=100, pady=30)

# Text input's style
click_sinistro.config(background='#1b1b1b', fg='white', font='Helvetica')

# Making the text input
click_destro = tk.Entry()

# Text input's position
click_destro.grid(row=2, column=0, sticky="WE", padx=100, pady=20)

# Text input's style
click_destro.config(background='#1b1b1b', fg='white', font='Helvetica')

