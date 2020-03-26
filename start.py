from pypresence import Presence
import time
import os
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
    arg = "-n" if os.name == "nt" else "-c"
    command = ["ping", "-w", "3", arg, "1", consoles["ip"]]
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


print("Service started...")
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
                        print("Connected.")
                    dscCnt = 0
                    if consoles["console"] == 4:
                        cname = consoles["custom"]
                    else:
                        cname = CONSOLE_NAMES[consoles["console"]]
                    if not connected:
                        print(f"Your {cname}[{consoles['ip']}] turned on! Have fun!")
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
                            print("Device turned off.")
                            RPC.close()
                            connected = False
                            disConnected = True
                        else:
                            dscCnt += 1
                            print(f"Connection lost... ( {dscCnt} / 2 )")
                time.sleep(5)
                ping = send_ping()
                return_node = ping.wait()
