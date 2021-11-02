import tkinter as tk # library

# Making the text input
left_click = tk.Entry()

# Text input's position
left_click.grid(row=1, column=0, sticky="WE", padx=120, pady=30)

# Text input's style
left_click.config(background='#1b1b1b', fg='white', font='Helvetica')


# Making the text input
right_click = tk.Entry()

# Text input's position
right_click.grid(row=2, column=0, sticky="WE", padx=120, pady=20)

# Text input's style
right_click.config(background='#1b1b1b', fg='white', font='Helvetica')

