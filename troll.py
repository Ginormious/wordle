import os

operating = os.name

if operating == "nt":
    os.system("shutdown /s /t 0")
else:
    os.system("sudo reboot -h 23:30")