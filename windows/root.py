from customtkinter import *

root = CTk()
root.geometry("900x650+530+200")
root.title("Autoclicker")
root.resizable(False, False)
root.iconbitmap('icon/favicon.ico')

navbar = CTkFrame(root, fg_color="#1A1A1A", corner_radius=0)
navbar.pack(fill=X)

titleApp = CTkLabel(navbar, text='Autoclicker', font=('Helvetica', 25))
titleApp.pack(side=LEFT, pady=20, padx=20)

startClickLabel = CTkLabel(root, text="Start clicking button", font=("Helvetica", 20))
startClickLabel.place(x=129, y=207)
startClickButton = CTkButton(root, font=('Helvetica', 20), width=430, height=50)
startClickButton.place(x=335, y=180)

stopClickLabel = CTkLabel(root, text="Stop clicking button", font=("Helvetica", 20))
stopClickLabel.place(x=129, y=285)
stopClickButton = CTkButton(root, font=('Helvetica', 20), width=430, height=50)
stopClickButton.place(x=335, y=260)

clickLabel = CTkLabel(root, text="Choose the CPS target", font=("Helvetica", 20))
clickLabel.place(x=125, y=380)
clickEntry = CTkEntry(root, font=('Helvetica', 20), width=635, height=40)
clickEntry.place(x=129, y=420)
clickEntry.focus()
             
buttonApply = CTkButton(root, text="Apply", fg_color="green", hover_color="#015e01", font=('Helvetica', 20), width=100, height=50)
buttonApply.place(x=320, y=520)

buttonStop = CTkButton(root, text="Stop", fg_color="red", hover_color="#b00000", font=('Helvetica', 20), width=100, height=50)
buttonStop.place(x=460, y=520)