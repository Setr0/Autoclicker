from tkinter import *

root = Tk()
root.geometry("900x650+530+200")
root.title("Autoclicker")
root.resizable(False, False)
root.config(bg='#121212')
root.iconbitmap('icon/favicon.ico')

titleApp = Label(root, text='Autoclicker', font=('Helvetica', 30), fg=('white'), background='#121212')
titleApp.place(x=350, y=60)

startClickLabel = Label(root, text="Start clicking button", fg="white", background='#121212', font=("Helvetica", 15))
startClickLabel.place(x=129, y=207)
startClickButton = Button(root, disabledforeground="white", bg='#198754', highlightthickness=0, font=('Helvetica', 20), fg='white', activebackground='#115433', activeforeground="white")
startClickButton.place(x=335, y=180, width=430, height=50)

stopClickLabel = Label(root, text="Stop clicking button", fg="white", background='#121212', font=("Helvetica", 15))
stopClickLabel.place(x=129, y=285)
stopClickButton = Button(root, disabledforeground="white", bg='#dc3545', highlightthickness=0, font=('Helvetica', 20), fg='white', activebackground='#99252f', activeforeground="white")
stopClickButton.place(x=335, y=260, width=430, height=50)

clickLabel = Label(root, text="Number of clicks", fg="white", background='#121212', font=("Helvetica", 15))
clickLabel.place(x=125, y=380)
clickEntry = Entry(background='#121212', highlightcolor="white", highlightbackground="white", highlightthickness=1, disabledbackground='#1c1c1c', disabledforeground="white", fg='white', font=('Helvetica', 20), insertbackground='white')
clickEntry.place(x=129, y=420, width=635, height=40)
clickEntry.focus()
             
buttonApply = Button(text="Apply", disabledforeground="white", background='#198754', font=('Helvetica', 20), fg='white', activebackground='#115433', activeforeground="white")
buttonApply.place(x=320, y=520, width=100, height=50)

buttonStop = Button(text="Stop", disabledforeground="white", background='#dc3545', font=('Helvetica', 20), fg='white', activebackground='#99252f', activeforeground="white")
buttonStop.place(x=460, y=520, width=100, height=50)