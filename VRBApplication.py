# Sports Village Registration and Booking System
# Prototype for Membership management
# Copyright 2019 Michael Stuart <mike@inf0web.com>
# Part of MSc Software Development 2019

from vrb.gui import *
import wx

if __name__ == '__main__':
    app = wx.App()
    frame = ManagerUI()
    frame.Show()
    app.MainLoop()
