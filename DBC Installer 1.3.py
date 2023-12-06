#-------------------------------------------------------------------------------
# Name:               DBC Installer
# Purpose:            Install necesarry components needed for DBC
#
# Created:            19 09 2022
# Developed by:       (c) MS Productions
#
# Lead Dev:           Meit Sant
# Lead QA:            Roshan Boby
#-------------------------------------------------------------------------------
from os import system
import multiprocessing as mp

def run_cmd(att):
    cmd = "pip install "+att
    system(cmd)

dependencies = [
    ('datetime'),
    ('pystray'),
    ('Pillow'),
    ('Pywin32'),
    ('Psutil'),
    ('Pystruct')
]
process_list = []

for i in dependencies:
    process_list.append(mp.Process(target=run_cmd, args=(i,)))

if __name__ == '__main__':
    for process in process_list:
      process.start()

    for process in process_list:
      process.join()
