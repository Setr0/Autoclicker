# Libraries
import tkinter as tk
from tkinter import CENTER

# Window configs
window = tk.Tk()  # Window
# Icon, only .ico files, for .ico files go to: https://www.icoconverter.com/
window.iconbitmap('favicon.ico')
window.geometry('900x650+500+200')  # Window's size and position
window.title("Autoclicker")  # Window's title
window.grid_columnconfigure(0, weight=1)  # Collumn configuration
window.config(bg="#1b1b1b")  # Window's background
window.resizable(False, False)  # The window isn't resizable
