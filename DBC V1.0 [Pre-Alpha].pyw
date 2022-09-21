#-------------------------------------------------------------------------------
# Name:        Desktop Background Changer V1.7
# Purpose:     Dynamically change desktop
#
# Author:      Meit - PC
#
# Created:     18 09 2022
# Copyright:   (c) Meit - PC 2022
#-------------------------------------------------------------------------------
import pystray,PIL.Image,datetime,struct,ctypes,time,sys
current_time = datetime.datetime.now()
SPI_SETDESKWALLPAPER = 20
print("Program running")

def Exit():
    icon.stop()
    sys.exit()

def is_64_windows():
    """Find out how many bits is OS. """
    return struct.calcsize('P') * 8 == 64

def get_sys_parameters_info():
    """Based on if this is 32bit or 64bit returns correct version of SystemParametersInfo function. """
    return ctypes.windll.user32.SystemParametersInfoW if is_64_windows() \
        else ctypes.windll.user32.SystemParametersInfoA

def get_time():
    hr = current_time.hour
    if hr>6:
        hr_ = (hr*1000)-5000
    elif hr<6:
        hr_ = (hr*1000)+19000
    path = "muk\muk"+str(hr_) + ".png"
    path = r"C:\Users\Meit - PC\Desktop\Python Programs\DBC\Bgs"+path
    WALLPAPER_PATH = path.replace("muk","")
    return WALLPAPER_PATH

def change_wallpaper():
    sys_parameters_info = get_sys_parameters_info()
    r = sys_parameters_info(SPI_SETDESKWALLPAPER, 0, WALLPAPER_PATH, 3)
    print("wallpaper changed",WALLPAPER_PATH)

    # When the SPI_SETDESKWALLPAPER flag is used,
    # SystemParametersInfo returns TRUE
    # unless there is an error (like when the specified file doesn't exist).
    if not r:
        print(ctypes.WinError())

def multiple():
    hr = current_time.hour
    print(hr)
    if hr>6:
        hr_ = (hr*1000)-5000
    elif hr<6:
        hr_ = (hr*1000)+19000
    print(hr_)
    path = "muk\muk"+str(hr_) + ".png"
    path = r"C:\Users\Meit - PC\Desktop\Python Programs\DBC\Bgs"+path
    WALLPAPER_PATH = path.replace("muk","")
    print(WALLPAPER_PATH)
    change_wallpaper()

image = PIL.Image.open("DBC.ico")
icon = pystray.Icon("DBC",image, menu=pystray.Menu(
    pystray.MenuItem("Refresh", multiple),
    pystray.MenuItem("Exit", Exit)
))

icon.run()
print("Icon running")

'''
while 2>1:
    change_wallpaper()
    time.sleep(4)
'''