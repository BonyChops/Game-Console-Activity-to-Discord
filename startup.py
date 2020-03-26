import os

if os.name != "nt":
    print("I'm sorry but this will work for Windows only...")
    print("Press enter to close...")
    gomi = input()
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


print("Setup to run this app when you booted up this PC, Okay?")
print("起動時にこのアプリを起動するよう設定します。よろしいですか？\n")
input("Press enter to continue...")

create_short_cut(f"{os.getcwd()}/start.exe", "GameConsoleActivitytoDiscord")
print("Done!")
input("Press enter to close...")
