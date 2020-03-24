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

# Releases (Download)
### Build for windows  
### [Releases](./releases)

# Pre-configure for Mac/Linux and other OS
1. Install python3
1. Run `git clone https://github.com/BonyChops/Game-Console-Activity-to-Discord.git` to download this repository.
1. `cd Game-Console-Activity-to-Discord`
1. `pip install -r requirements.txt`  
(If you want to use latest version of package, run  
`pip install https://github.com/qwertyquerty/pypresence/archive/master.zip` )
1. [<span style="color: red; ">IMPORTANT</span>] This script is made for windows so you have to change a little bit.  
Please modify `start.py` like this...  

[start.py:24]  
`... (["ping", "-w", "3", "`<span style="color: red; ">-n</span>`", "1", ...`  
↓  
`... (["ping", "-w", "3", "`<span style="color: green; ">-c</span>`", "1", ...`  
[start.py:32]  
`... (["ping", "-w", "3", "`<span style="color: red; ">-n</span>`", "1", ...`  
↓  
`... (["ping", "-w", "3", "`<span style="color: green; ">-c</span>`", "1", ...`  


6. Done! Go on to the next section: [Setup for windows](#setup-for-windows) (and also for other os)

# Setup for windows
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
