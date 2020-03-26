English｜[日本語 (Japanese)](https://github.com/BonyChops/Game-Console-Activity-to-Discord/blob/master/README_ja.md)
# Game Console Activity to Discord
Share your ACTUAL game console activity on Discord!
# Features
Check whether your game consoles on your local network is active or not and make it able to see it with your Discord's profile.  

<div align="center">

<img src="https://raw.githubusercontent.com/bonychops/Game-Console-Activity-to-Discord/img/status.png" alt="Profile" title="Profile"><br><br>
<img src="https://raw.githubusercontent.com/bonychops/Game-Console-Activity-to-Discord/img/profile.png" alt="Profile" title="Profile">
</div>

# Supported Game Consoles
This app supported most of the game consoles which will automatically connect to the internet.  
Such as...  
- Nintendo Switch
- Nintendo 3DS
- PS3
- PS4

# Easy Setup (Japanese)

[![Setup Video](https://img.youtube.com/vi/5yHuvOHLPRc/0.jpg)](https://www.youtube.com/watch?v=5yHuvOHLPRc)

[Discordにゲーム機のステータスを出すアプリ作りました - YouTube](https://www.youtube.com/watch?v=5yHuvOHLPRc)

# Releases (Download)
### Build for windows  
### [Releases](https://github.com/BonyChops/Game-Console-Activity-to-Discord/releases)

# Pre-configure for Mac/Linux and other OS
0. This app will work for OS which can use Python3 and Discord native app.
1. Install python3
1. Run `git clone https://github.com/BonyChops/Game-Console-Activity-to-Discord.git` to download this repository.
1. `cd Game-Console-Activity-to-Discord`
1. Run `pip3 install -r requirements.txt` to install package.
1. Done! Go on to the next section: [Setup for windows](#setup-for-windows) (and also for other os)

# Setup for Windows (and other OS)
0. If you are using not Windows, you have to do [this](#pre-configure-for-maclinux-and-other-os) first. 
1. Run `config.exe` (`config.py`) to start configuration.
1. Add your console infomation  
Here is some example...
```
Configuration
[0] Add new console
[1] Delete console
[2] Exit

Type number [0-2]?
0

Select your Game Console!
[0] Nintendo Switch
[1] Nintendo 3DS
[2] PS3
[3] PS4
[4] Others

Type number [0-4]?
0
Type IP address of your console!
192.168.1.30
Added!
------------------------------
[Nintendo Switch] IP 192.168.1.30
------------------------------

Configuration
[0] Add new console
[1] Delete console
[2] Exit

Type number [0-2]?
2
Goodbye.
```
You have to realise what is your IP address of your consoles.  
If your console is Nintendo Switch, you can find it here  
- [Settings] - [Internet] - [Connection Status] - [IP Address]
- [設定] - [インターネット] - [接続状況] - [IPアドレス] 
3. Done! Easy-peasy!
2. Run `start.exe` (`start.py`). It will change your Discord profile automatically.

# Run app automatically when you booted up pc (Win only)
Just run `startup.exe`  
It don't require admin rights.

# Package
### qwertyquerty/pypresence - Github

[![pypresence](https://img.shields.io/badge/using-pypresence-00bb88.svg?style=for-the-badge&logo=discord&logoWidth=20)](https://github.com/qwertyquerty/pypresence)