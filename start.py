from pypresence import Presence
import time
import os
import platform
import json
import subprocess

CLIENT_IDS = [
    "691885764124082186",
    "691919061336195114",
    "691925175049912380",
    "691920993438007347",
    "691892857149063200"
]
CUSTOM_NAMES = [
    "nintendo-switch",
    "nintendo-3ds",
    "ps3",
    "ps4",
    "others"
]
CONSOLE_NAMES = [
    "Nintendo Switch",
    "Nintendo 3DS",
    "Play Station 3",
    "Play Station 4"
]


def send_ping():
    arg  = "-n" if platform.system() == "Windows" else "-c"
    arg2 = "-W" if platform.system() == "Darwin" else "-w"
    command = ["ping", arg2, "3", arg, "1", consoles["ip"]]
    return subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )


config = {}
try:
    with open("config.json", "r") as f:
        config = json.load(f)
except:
    input("First you have to run config.py(config.exe) to config.\nPress enter to exit...")
    exit()


if not os.path.exists("./lang/lang.txt"):
    input("Can't find lang.txt file. You have to run config.py(config.exe) to config.\nPress enter to exit...")
    exit()
else:
    with open("./lang/lang.txt", "r", encoding="utf-8") as f:
        lang = f.read()


message = {}
with open(f'./lang/{lang}.json', "r", encoding="utf-8") as f:
    message = json.load(f)


print(message["start"])
while True:
    for consoles in config:
        client_id = CLIENT_IDS[consoles["console"]]
        custom = CUSTOM_NAMES[consoles["console"]]
        ping = send_ping()
        time.sleep(1)
        return_node = ping.wait()
        if return_node == 0:
            disConnected = False
            connected = False
            dscCnt = 0
            while not disConnected:
                # print("ping returned {0}".format(return_code))
                # print(ping.stdout.read().decode("cp932"))
                if return_node == 0:
                    if dscCnt != 0:
                        print(message["connected"])
                    dscCnt = 0
                    if consoles["console"] == 4:
                        cname = consoles["custom"]
                    else:
                        cname = CONSOLE_NAMES[consoles["console"]]
                    if not connected:
                        print(message["turned_on"].format(cname, consoles["ip"]))
                        RPC = Presence(client_id)
                        RPC.connect()  # Start the handshake loop
                        if 0 <= consoles["console"] <= 3:
                            # Set the presence)
                            RPC.update(start=time.time(), large_image=custom, large_text=cname)
                        else:
                            # Set the presence)
                            RPC.update(start=time.time(), state=cname, large_image="others", large_text=cname)
                        connected = True
                else:
                    if connected:
                        if dscCnt == 2:
                            print(message["turned_off"])
                            RPC.close()
                            connected = False
                            disConnected = True
                        else:
                            dscCnt += 1
                            print(message["connection_lost"].format(dscCnt))
                time.sleep(5)
                ping = send_ping()
                return_node = ping.wait()
