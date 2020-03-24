from pypresence import Presence, Activity
import time
import os
import json
import subprocess

if not os.path.exists('config.json'):
    print("First you have to run config.py(config.py) to config.\nPress enter to exit...")
    gomi = input()
    exit()
f = open("config.json", 'r')
config = json.load(f)
f.close()
client_ids = ["691885764124082186","691919061336195114","691925175049912380","691920993438007347","691892857149063200"]
custom_names = ["nintendo-switch","nintendo-3ds","ps3","ps4","others"]
console_names = ["Nintendo Switch","Nintendo 3DS","Play Station 3","Play Station 4"]


print("Service started...")
while True:
    for consoles in config:
        client_id = client_ids[consoles['console']]
        custom = custom_names[consoles['console']]
        ping = subprocess.Popen(["ping", "-w", "3", "-n", "1", consoles['ip']], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        time.sleep(1)
        returncode = ping.wait()
        if returncode == 0:
            disConnected = False
            connected = False
            dscCnt = 0
            while disConnected == False:
                ping = subprocess.Popen(["ping", "-w", "3", "-n", "1", consoles['ip']], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                returncode = ping.wait()
                #print('ping returned {0}'.format(returncode))
                #print(ping.stdout.read().decode('cp932'))
                if returncode == 0:
                    if dscCnt != 0:
                        print("Connected.")
                    dscCnt = 0
                    if consoles['console'] == 4:
                        cname = consoles['custom']
                    else:
                        cname = console_names[consoles['console']]
                    if connected != True:
                        print("Your %s[%s] turned on! Have fun!" % (cname,consoles['ip']))
                        RPC = Presence(client_id)
                        RPC.connect() # Start the handshake loop
                        if 0 <= consoles['console'] <= 3:
                            RPC.update( start=time.time(), large_image=custom, large_text=cname)  # Set the presence)
                        else:
                            RPC.update( start=time.time(),state=cname, large_image="others", large_text=cname)  # Set the presence)    
                        connected = True
                else:
                    if dscCnt == 2:
                        if connected != False:
                            print("Device turned off.")
                            RPC.close()
                            connected = False
                            disConnected = True
                    else:
                        dscCnt += 1
                        print("Connection lost... (",dscCnt," / 2 )")
                time.sleep(5)