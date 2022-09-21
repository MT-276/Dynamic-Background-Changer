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
print("Current Hour = ",hr)
if hr>6:
    hr_ = (hr*1000)-5000
elif hr<6:
    hr_ = (hr*1000)+19000
print("File no. ",hr_)
bg_number = "muk\muk"+str(hr_) + ".png"
path = r"C:\Users\Meit - PC\Desktop\Python Programs\DBC\Bgs"+bg_number
WALLPAPER_PATH = path.replace("muk","")
print("path = ",WALLPAPER_PATH,"\n")
set_wallpaper(WALLPAPER_PATH)

'''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~ System Tray ~~~~~~~~~~~~~~~~~~~~~~~~
image = PIL.Image.open("DBC.ico")
def Exit():
    icon.stop()
icon = pystray.Icon("DBC",image, menu=pystray.Menu(
    pystray.MenuItem("Exit", Exit)
))

icon.run()
'''