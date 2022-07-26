from tkinter import *

window = Tk()
window.geometry("900x650+530+200")
window.title("Autoclicker")
window.resizable(False, False)
window.config(bg='#212529')
window.iconbitmap('favicon.ico')

titleApp = Label(window, text='Autoclicker', font=('Helvetica', 30), fg=('white'), background=('#212529'))
titleApp.place(x=350, y=80)

istrunctions = Label(window, text='''1 click = 10 CPS 
                        \nPress 1 for starting left mouse button spamming and press 2 for stopping''',
                         font=('Helvetica', 15),
                         fg=('white'),
                         background=('#212529'))  
istrunctions.place(x=125, y=180)
             
buttonApply = Button(text="Apply", background='#198754', font=('Helvetica', 20), fg='white', activebackground='#115433', activeforeground="white")
buttonApply.place(x=320, y=460, width=100, height=50)

buttonStop = Button(text="Stop", background='#dc3545', font=('Helvetica', 20), fg='white', activebackground='#99252f', activeforeground="white")
buttonStop.place(x=460, y=460, width=100, height=50)

clickEntry = Entry(background='#212529', fg='white', font=('Helvetica', 20), insertbackground='white')
clickEntry.place(x=130, y=300, width=635, height=40)
clickEntry.insert(0, "Number of clicks")