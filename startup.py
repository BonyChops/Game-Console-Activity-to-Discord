import os
import json


if not os.path.exists("./lang/lang.txt"):
    input("Can't find lang.txt file. You have to run config.py(config.exe) to config.\nPress enter to exit...")
    exit()
else:
    with open("./lang/lang.txt", "r", encoding="utf-8") as f:
        lang = f.read()


message = {}
with open(f'./lang/{lang}.json', "r", encoding="utf-8") as f:
    message = json.load(f)


if os.name != "nt":
    input(message["win_only"])
    exit()


import win32com.client


def create_short_cut(path, sc_file_name, icon=None):
    if icon is None:
        icon = path

    shell = win32com.client.Dispatch("WScript.shell")

    sh_cut = shell.CreateShortcut(
        os.path.join(f"C:/Users/{os.getlogin()}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup",
                     f"{sc_file_name}.lnk"))
    sh_cut.TargetPath = path
    sh_cut.WindowStyle = 1
    sh_cut.IconLocation = icon
    sh_cut.WorkingDirectory = f"C:/Users/{os.getlogin()}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup"

    sh_cut.Save()

try:
    input(message["confirm_startup"])
except:
    print(message["canceled"])
    exit()

create_short_cut(f"{os.getcwd()}/start.exe", "GameConsoleActivitytoDiscord")
input(message["startup_done"])