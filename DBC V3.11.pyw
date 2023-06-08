
#-------------------------------------------------------------------------------
# Name:               Dynamic Background Changer v3.11
#
# Created:            19 09 2022
# Developed by:       (c) MS Productions
#
# Lead Dev:           Meit Sant
# Lead QA:            Roshan Boby
#-------------------------------------------------------------------------------

#~~~~~~~~~~~~~~~~~~~~ User Preferences ~~~~~~~~~~~~~~~~~~~


Refresh_time = 5       #In seconds
Folder_path = r"  > Your path here <   "


#~~~~~~~~~~~~~~~~~~~~ Prerequisites ~~~~~~~~~~~~~~~~~~~
def is_64_windows():
    """Find out how many bits is OS. """
    return struct.calcsize('P') * 8 == 64
def get_sys_parameters_info():
    """Based on if this is 32bit or 64bit returns correct version of SystemParametersInfo function. """
    return ctypes.windll.user32.SystemParametersInfoW if is_64_windows() \
        else ctypes.windll.user32.SystemParametersInfoA
def getWallpaper():
    ubuf = ctypes.create_unicode_buffer(512)
    ctypes.windll.user32.SystemParametersInfoW(win32con.SPI_GETDESKWALLPAPER,len(ubuf),ubuf,0)
    return ubuf.value
def change_wallpaper():
    current_time = datetime.datetime.now()
    hr = current_time.hour
    if hr>6:
        hr_ = (hr*1000)-5000
    elif hr<6:
        hr_ = (hr*1000)+19000
    elif hr == 6:
        hr_ = 1000
    path = "muk\muk"+str(hr_) + ".png"
    path = Folder_path+path
    WALLPAPER_PATH = path.replace("muk","")
    current_bg = getWallpaper()
    if current_bg != WALLPAPER_PATH:
        sys_parameters_info = get_sys_parameters_info()
        r = sys_parameters_info(SPI_SETDESKWALLPAPER, 0, WALLPAPER_PATH, 3)
        if not r:
            Error_Disp("Could not find image\n\n(ERROR CODE -0x23494576)")
def proc_kill(PROCNAME):
    for proc in psutil.process_iter():
        # check whether the process name matches
        if proc.name() == PROCNAME:
            proc.kill()
def Exit():
    icon.stop()
    proc_kill("python.exe")
    sys.exit()
    quit()
def Error_Disp(Message):
    root = Tk()
    root.title("Error")
    root.geometry('300x95')

    a = Label(root, text =Message)
    btn = Button(root, text = 'Ok', bd = '5',command = root.destroy)

    a.pack(side = 'top')
    btn.pack(side = 'bottom')
    root.mainloop()
    sys.exit()
#~~~~~~~~~~~~~ Main Multiprocessing Pools ~~~~~~~~~~~~~

def looping_the_cw():
    while True:
        change_wallpaper()
        time.sleep(Refresh_time)
def tray_icon():
    icon.run()

#~~~~~~~~~~~~~~~~~~~~~~ Program ~~~~~~~~~~~~~~~~~~~~~~~
try:
    import win32con,pystray,psutil,PIL.Image,datetime,struct,ctypes,time,sys,os
    from tkinter import *
    import multiprocessing as mp
except:
    import sys
    from tkinter import *
    Error_Disp("You have not run the installer. \nPlease run the Installer first \n\n(ERROR CODE -0x9348734A)")
#Refresh_time = Refresh_time *60
SPI_SETDESKWALLPAPER = 20
if os.path.exists(Folder_path) == False:
    Error_Disp("The specified path doesn't exist.\nPlease try again \n\n(ERROR CODE -0x46573445)")
try:
    image = PIL.Image.open("DBC.ico")
except:
    Error_Disp("Tray Icon not found\n Please verify download location of the icon file \n\n(ERROR CODE -0x39458784)")

icon = pystray.Icon("DBC",image, menu=pystray.Menu(
        pystray.MenuItem("Refresh", change_wallpaper),
        pystray.MenuItem("Exit", Exit)
    ))
p1 = mp.Process(target=looping_the_cw)
p2 = mp.Process(target=tray_icon)

if __name__ == '__main__':
    p1.start()
    p2.start()
    p1.join()
    p2.join()

