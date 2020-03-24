import os
import win32com.client

def createShortCut(path,scFileName,icon=None):
    if icon == None:
        icon = path

    shell   = win32com.client.Dispatch('WScript.shell')

    shCut                  = shell.CreateShortcut(os.path.join('C:/Users/'+os.getlogin()+'/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup',scFileName+".lnk"))
    shCut.TargetPath       = path
    shCut.WindowStyle      = 1
    shCut.IconLocation     = icon
    shCut.WorkingDirectory = 'C:/Users/'+os.getlogin()+'/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup'

    shCut.Save()

print("Setup to run this app when you booted up this PC, Okay?")
print("起動時にこのアプリを起動するよう設定します。よろしいですか？\n")
print("Press enter to continue...")
gomi = input()

createShortCut(os.getcwd()+'start.exe','GameConsoleActivitytoDiscord')
print("Done!")
print("Press enter to close...")
gomi = input()
