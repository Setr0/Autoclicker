from window import window, clickEntry, buttonApply, buttonStop
from autoClicker import run, stop
from widgetsFunctions import delete, hoverOnApply, hoverOffApply, hoverOnStop, hoverOffStop

buttonApply.config(command=run)
buttonApply.bind('<Enter>', hoverOnApply)
buttonApply.bind('<Leave>', hoverOffApply)

buttonStop.config(command=stop)
buttonStop.bind('<Enter>', hoverOnStop)
buttonStop.bind('<Leave>', hoverOffStop)

clickEntry.bind("<1>", delete)

if __name__ == '__main__':
    window.mainloop() 