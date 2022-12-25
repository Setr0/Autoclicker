from customtkinter import *

root = CTk()
root.geometry("900x650+530+200")
root.title("Autoclicker")
root.resizable(False, False)
root.iconbitmap('icon/favicon.ico')

titleApp = CTkLabel(root, text='Autoclicker', font=('Helvetica', 30))
titleApp.pack(pady=20)

startClickLabel = CTkLabel(root, text="Start clicking button", font=("Helvetica", 20))
startClickLabel.place(x=129, y=207)
startClickButton = CTkButton(root, font=('Helvetica', 20))
startClickButton.place(x=335, y=180, width=430, height=50)

stopClickLabel = CTkLabel(root, text="Stop clicking button", font=("Helvetica", 20))
stopClickLabel.place(x=129, y=285)
stopClickButton = CTkButton(root, font=('Helvetica', 20))
stopClickButton.place(x=335, y=260, width=430, height=50)

clickLabel = CTkLabel(root, text="Choose the CPS target", font=("Helvetica", 20))
clickLabel.place(x=125, y=380)
clickEntry = CTkEntry(root, font=('Helvetica', 20))
clickEntry.place(x=129, y=420, width=635, height=40)
clickEntry.focus()
             
buttonApply = CTkButton(root, text="Apply", font=('Helvetica', 20))
buttonApply.place(x=320, y=520, width=100, height=50)

buttonStop = CTkButton(root, text="Stop", font=('Helvetica', 20))
buttonStop.place(x=460, y=520, width=100, height=50)