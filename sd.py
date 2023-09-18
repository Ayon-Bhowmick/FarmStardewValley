import os
from sys import platform
import shutil
from datetime import date, datetime
import pytz
import subprocess

SAVE_PATH_WIN = "C:\\Users\\{os.getlogin()}\\AppData\\Roaming\\StardewValley\\Saves"
# TODO: add save file name

def push():
    shutil.copyfile(save_path, os.getcwd() + f"\\{FILENAME}")
    os.system("git add *")
    current_time = datetime.now(pytz.timezone("America/New_York"))
    current_time_str = current_time.strftime("%H:%M:%S")
    os.system(f"git commit -m \"Saved {date.today()} {current_time_str}\"")
    os.system("git push")

def pull():
    if out := "Already up to date." not in str(subprocess.check_output("git pull", shell=True)):
        shutil.copyfile(f"./{FILENAME}", save_path)
    return out


