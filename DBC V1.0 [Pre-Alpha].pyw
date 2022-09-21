#-------------------------------------------------------------------------------
# Name:        Desktop Background Changer V1.0
# Purpose:
#
# Author:      Meit - PC
#
# Created:     18 09 2022
# Copyright:   (c) Meit - PC 2022
#-------------------------------------------------------------------------------
import pystray,PIL.Image,datetime
from wallpaper import set_wallpaper

current_time = datetime.datetime.now()
hr = current_time.hour
path = str(hr*1000) + ".png"

set_wallpaper(path)




image = PIL.Image.open(r"C:\Users\Meit - PC\Desktop\DBC\DBC.ico")
def on_clicked(icon, item):
    print("Hello world")
def Exit():
    icon.stop()

icon = pystray.Icon("DBC",image, menu=pystray.Menu(
    pystray.MenuItem("Say Hello", on_clicked),
    pystray.MenuItem("Exit", Exit)
))

icon.run()