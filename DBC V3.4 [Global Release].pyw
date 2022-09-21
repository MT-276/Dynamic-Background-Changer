#-------------------------------------------------------------------------------
# Name:        Dynamic Background Changer v3.4 [Global Release copy]
#
# Author:      MS Productions
#
# Created:     19 09 2022
# Copyright:   (c) MS Productions
#-------------------------------------------------------------------------------

#~~~~~~~~~~~~~~~~~~~~ User Preferences ~~~~~~~~~~~~~~~~~~~


Refresh_time = 0.5         #In minutes
Folder_path = r" Your folder path here "


#~~~~~~~~~~~~~~~~~~~~ Prerequisites ~~~~~~~~~~~~~~~~~~~

def is_64_windows():
    """Find out how many bits is OS. """
    return struct.calcsize('P') * 8 == 64
def get_sys_parameters_info():
    """Based on if this is 32bit or 64bit returns correct version of SystemParametersInfo function. """
    return ctypes.windll.user32.SystemParametersInfoW if is_64_windows() \
        else ctypes.windll.user32.SystemParametersInfoA
def change_wallpaper():
    current_time = datetime.datetime.now()
    hr = current_time.hour
    if hr>6:
        hr_ = (hr*1000)-5000
    elif hr<6:
        hr_ = (hr*1000)+19000
    path = "muk\muk"+str(hr_) + ".png"
    path = Folder_path+path
    WALLPAPER_PATH = path.replace("muk","")
    sys_parameters_info = get_sys_parameters_info()
    r = sys_parameters_info(SPI_SETDESKWALLPAPER, 0, WALLPAPER_PATH, 3)
    if not r:
        print(ctypes.WinError())
def Exit():
    icon.stop()
    beta = 1
    sys.exit()
    quit()
def kill():
        root.destroy()
        sys.exit()
#~~~~~~~~~~~~~ Main Multiprocessing Pools ~~~~~~~~~~~~~

def looping_the_cw():
    while beta==0:
        current_time = datetime.datetime.now()
        hr = current_time.hour
        if hr>6:
            hr_ = (hr*1000)-5000
        elif hr<6:
            hr_ = (hr*1000)+19000
        path = "muk\muk"+str(hr_) + ".png"
        path = r"C:\Users\Meit - PC\Desktop\Python Programs\DBC\Bgs"+path
        WALLPAPER_PATH = path.replace("muk","")
        change_wallpaper()
        time.sleep(Refresh_time)
def tray_icon():
    icon.run()

#~~~~~~~~~~~~~~~~~~~~~~ Program ~~~~~~~~~~~~~~~~~~~~~~~
try:
    import pystray,PIL.Image,datetime,struct,ctypes,time,sys,os
    from tkinter import *
    import multiprocessing as mp
except:
    import sys
    from tkinter import *
    root = Tk()
    root.title("Error")
    root.geometry('300x80')

    a = Label(root, text ="You have not run the installer. \nPlease run the Installer first")
    btn = Button(root, text = 'Ok', bd = '5',command = kill)

    a.pack(side = 'top')
    btn.pack(side = 'bottom')
    root.mainloop()
    sys.exit()
Refresh_time = Refresh_time *60
SPI_SETDESKWALLPAPER = 20
import os
if os.path.exists(Folder_path) == False:
    from tkinter import *
    root = Tk()
    root.title("Error")
    root.geometry('300x80')

    a = Label(root, text ="The specified path doesn't exist.\nPlease try again")
    btn = Button(root, text = 'Ok', bd = '5',command = kill)

    a.pack(side = 'top')
    btn.pack(side = 'bottom')
    root.mainloop()

image = PIL.Image.open("DBC.ico")
icon = pystray.Icon("DBC",image, menu=pystray.Menu(
        pystray.MenuItem("Refresh", change_wallpaper),
        pystray.MenuItem("Exit", Exit)
    ))
beta = 0
p1 = mp.Process(target=looping_the_cw)
p2 = mp.Process(target=tray_icon)

if __name__ == '__main__':
    p1.start()
    p2.start()
    p1.join()
    p2.join()
