#! python3

'''
V 1.0 GUI serial interface for robot - allows to define
bytecodes to be sent, logs data
'''

import json
from tkinter import *
import serial
import io

#create a class container for the main app loop

class AppWindow:
    frame = None
    widgets = []
    #initialization - place buttons here
    def __init__(self, root):
        self.frame = Frame(root)
        self.frame.pack()

'''
addWidgetFxn takes a functional and optional keywords and pack function to create a widget.
widgetFxn should be a function that returns a widget, for example Button(), and kwd is a
dictionary with keywords for that function.
packFxn is an optional substitute to choose how to pack the widget (and can actually execute
arbitrary code - good hack for init stuff). Should be take the widget as an argument - ex:

lambda widget : widget.pack(side = LEFT)

'''
def addWidgetFxn(self, widgetFxn, kwd, packFxn = None):
    widget = widgetFxn(self.frame, kwd)
    if (packFxn): packFxn(widget)
    else: widget.pack()
    self.widgets.append(widget)

#Initial setup
root = Tk()
mainWindow = AppWindow(root)
mainWindow.addWidgetFxn(Button,kwd = {"text":"Hello World"}, packFxn = lambda obj : obj.pack(side = LEFT))


# Main application loop
root.mainloop()
