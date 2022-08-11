from windows.root import root, buttonApply, buttonStop, startClickButton, stopClickButton
from func.autoClicker import run, stop
from func.widgetsFunctions import hoverOnApply, hoverOffApply, hoverOnStartClick, hoverOnStop, hoverOffStop, hoverOffStartClick, hoverOnStartClick, hoverOnStopClick, hoverOffStopClick
import func.settings

startClickButton.config(text=func.settings.getStartSettings())
startClickButton.config(command=func.settings.startSettings)
startClickButton.bind('<Enter>', hoverOnStartClick)
startClickButton.bind('<Leave>', hoverOffStartClick)

stopClickButton.config(text=func.settings.getStopSettings())
stopClickButton.config(command=func.settings.stopSettings)
stopClickButton.bind('<Enter>', hoverOnStopClick)
stopClickButton.bind('<Leave>', hoverOffStopClick)

buttonApply.config(command=run)
buttonApply.bind('<Enter>', hoverOnApply)
buttonApply.bind('<Leave>', hoverOffApply)

buttonStop.config(command=stop)
buttonStop.bind('<Enter>', hoverOnStop)
buttonStop.bind('<Leave>', hoverOffStop)

if __name__ == '__main__':
    root.mainloop() 