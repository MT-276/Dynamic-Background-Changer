#-------------------------------------------------------------------------------
# Name:        DBC Installations
# Purpose:     Install necesarry components needed for DBC
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

dependencies = [
    ('pynput'),
    ('pyautogui'),
    ('datetime'),
    ('selenium'),
    ('openpyxl'),
    ('tkinter'),
    ('numpy'),
    ('pystray'),
    ('struct'),
    ('Pillow'),

]
process_list = []

for i in dependencies:
    process_list.append(mp.Process(target=run_cmd, args=(i,)))
if __name__ == '__main__':
    for process in process_list:
      process.start()

    for process in process_list:
      process.join()

finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')


