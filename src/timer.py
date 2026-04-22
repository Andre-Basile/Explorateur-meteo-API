from datetime import datetime
import locale 
locale.setlocale(locale.LC_TIME,'French_France')

class time:
    def __init__(self):
        pass

    def getFormalTime(self):
        date = datetime.now()
        date = date.strftime("%A %d %B %Y à %H:%M")
        return date.capitalize()


