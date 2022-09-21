#-------------------------------------------------------------------------------
# Name:        DBC Instalations
# Purpose:     Install necesarry components needer for DBC
#
# Author:      MS Productions
# Created:     19/09/2022
# Copyright:   (c) MS Productions 2022
#-------------------------------------------------------------------------------
import time ,sys , subprocess, os
import multiprocessing as mp

def run_cmd(att):
    cmd = "pip install "+att
    print(cmd)
    os.system(cmd)

print("[INFO] Running script -")
print("[INFO] Installing modules :")
start = time.perf_counter()

p1 = mp.Process(target=run_cmd,args=("pynput",))
p2 = mp.Process(target=run_cmd,args=("pyautogui",))
p3 = mp.Process(target=run_cmd,args=("datetime",))
p4 = mp.Process(target=run_cmd,args=("selenium",))
p5 = mp.Process(target=run_cmd,args=("openpyxl",))
p6 = mp.Process(target=run_cmd,args=("tkinter",))
p7 = mp.Process(target=run_cmd,args=("numpy",))
p8 = mp.Process(target=run_cmd,args=("pystray",))
p9 = mp.Process(target=run_cmd,args=("struct",))
p10 = mp.Process(target=run_cmd,args=("Pillow",))

if __name__ == '__main__':
    p1.start()
    print("p1 started")
    p2.start()
    print("p2 started")
    p3.start()
    print("p3 started")
    p4.start()
    print("p4 started")
    p5.start()
    print("p5 started")
    p6.start()
    print("p6 started")
    p7.start()
    print("p7 started")
    p8.start()
    print("p8 started")
    p9.start()
    print("p9 started")
    p10.start()
    print("p10 started")

    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
    p7.join()
    p8.join()
    p9.join()
    p1.join()

finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')