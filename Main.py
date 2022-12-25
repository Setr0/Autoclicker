from windows.root import *
from utils.autoClicker import *
import utils.settings as settings

if __name__ == '__main__':
    startClickButton.configure(text=settings.getStartSettings())
    startClickButton.configure(command=settings.startSettings)

    stopClickButton.configure(text=settings.getStopSettings())
    stopClickButton.configure(command=settings.stopSettings)

    buttonApply.configure(command=run)

    buttonStop.configure(command=stop)

    root.mainloop()
