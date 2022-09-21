#-------------------------------------------------------------------------------
# Name:        Desktop Background Changer V1.0
# Purpose:
#
# Author:      Meit - PC
#
# Created:     18 09 2022
# Copyright:   (c) Meit - PC 2022
#-------------------------------------------------------------------------------

from infi.systray import SysTrayIcon
def say_hello(systray):
    print("Hello, World!")
menu_options = (("Say Hello", None, say_hello),)
systray = SysTrayIcon("DBC.ico", "DBC V1.0", menu_options)
systray.start()