from window import clickEntry, buttonApply, buttonStop, END

def hoverOnApply(event):
    buttonApply.config(background='#156c41', fg="white")

def hoverOffApply(event):
    buttonApply.config(background='#198754', fg="white")

def hoverOnStop(event):
    buttonStop.config(background='#b32b37', fg="white")

def hoverOffStop(event):
    buttonStop.config(background='#dc3545', fg="white")

def delete(event):
    clickEntry.delete(0, END)