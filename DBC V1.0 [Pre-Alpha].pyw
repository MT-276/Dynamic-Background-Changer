import pystray,PIL.Image,datetime,struct,ctypes,time,sys
import multiprocessing as mp
SPI_SETDESKWALLPAPER = 20

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
    print(hr)
    if hr>6:
        hr_ = (hr*1000)-5000
    elif hr<6:
        hr_ = (hr*1000)+19000
    print(hr_)
    path = "muk\muk"+str(hr_) + ".png"
    path = r"C:\Users\Meit - PC\Desktop\Python Programs\DBC\Bgs"+path
    WALLPAPER_PATH = path.replace("muk","")
    sys_parameters_info = get_sys_parameters_info()
    r = sys_parameters_info(SPI_SETDESKWALLPAPER, 0, WALLPAPER_PATH, 3)
    print("wallpaper changed",WALLPAPER_PATH)
    if not r:
        print(ctypes.WinError())
def Exit():
    icon.stop()
    sys.exit()

#~~~~~~~~~~~~~ Main Multiprocessing Pools ~~~~~~~~~~~~~

def looping_the_cw():
    while 2>1:
        current_time = datetime.datetime.now()
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
        time.sleep(600)

def tray_icon():

    image = PIL.Image.open("DBC.ico")
    icon = pystray.Icon("DBC",image, menu=pystray.Menu(
        pystray.MenuItem("Refresh", change_wallpaper),
        pystray.MenuItem("Exit", Exit)
    ))

    icon.run()
    print("Icon running")

#~~~~~~~~~~~~~~~~~~~~~~ Program ~~~~~~~~~~~~~~~~~~~~~~~

p1 = mp.Process(target=looping_the_cw)
p2 = mp.Process(target=tray_icon)

if __name__ == '__main__':
    p1.start()
    p2.start()
    #p1.join()
    p2.join()

