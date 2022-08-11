from windows.root import buttonApply, buttonStop, startClickButton, stopClickButton, END

def hoverOnStartClick(event):
    startClickButton.config(background='#156c41', fg="white")

def hoverOffStartClick(event):
    startClickButton.config(background='#198754', fg="white")

def hoverOnStopClick(event):
    stopClickButton.config(background='#b32b37', fg="white")

def hoverOffStopClick(event):
    stopClickButton.config(background='#dc3545', fg="white")

def hoverOnApply(event):
    buttonApply.config(background='#156c41', fg="white")

def hoverOffApply(event):
    buttonApply.config(background='#198754', fg="white")

def hoverOnStop(event):
    buttonStop.config(background='#b32b37', fg="white")

def hoverOffStop(event):
    buttonStop.config(background='#dc3545', fg="white")