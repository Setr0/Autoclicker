import win10toast # Library
toaster = win10toast.ToastNotifier() # init win10toast
toaster.show_toast("Autoclicker", "Press 5 for to change the numbers", icon_path="favicon.ico") # Showing the notify
