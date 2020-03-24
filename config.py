import json
import os
config_json = []

def deleteConsole():
    global config_json
    
    cnt = 0
    print('-' * 30)
    for settings in config_json:
        if settings['console'] == 4:
            cname = settings['custom']
        else:
            cname = console_names[settings['console']]
        print("[%d]%-15s IP %s" % (cnt,cname,settings['ip']))
        cnt += 1
    print('-' * 30)
    endCode = cnt
    deleteNum = -1
    while not 0 <= deleteNum <= endCode:
        print("\nSelect console you want to delete (type [%d] to cancel)\nType number [0-%d]?" % (endCode,endCode))
        deleteNum = int(input())
    if deleteNum == endCode:
        return
    config_json.pop(deleteNum)
    print("Deleted.")



def addNewConsole():
    console = 100
    while not 0 <= console <= 4:
        print ("""
Select your Game Console!
[0] Nintendo Switch
[1] Nintendo 3DS
[2] PS3
[3] PS4
[4] Others

Type number [0-4]?""")
        console = int(input())
    jsonar = {'console' : console}
    if console == 4:
        print("Type your console name!")
        jsonar.update({'custom':input()})
    print("Type IP address of your console!")
    jsonar.update({'ip':input()})
    return jsonar

if not os.path.exists('config.json'):
    config_json = []
else:
    f = open("config.json","r")
    config_json = json.load(f)
    f.close()
console_names = ["Nintendo Switch","Nintendo 3DS","Play Station 3","Play Station 4"]
while True:
    if config_json != []:
        print('-' * 30)
        for settings in config_json:
            if settings['console'] == 4:
                cname = settings['custom']
            else:
                cname = console_names[settings['console']]
            print("[%-15s] IP %s" % (cname,settings['ip']))
        print('-' * 30)
    setting_option = 100
    while not 0 <= setting_option <= 2:
        print ("""
Configuration
[0] Add new console
[1] Delete console
[2] Exit

Type number [0-2]?""")
        setting_option = int(input())
    if setting_option == 2:
        print("Good bye")
        exit()

    if setting_option == 0:
        eachArray = addNewConsole()
        config_json.append(eachArray)
        fw = open('config.json','w')
        json.dump(config_json,fw)
        fw.close()
        print('Added!')

    if setting_option == 1:
        if config_json == []:
            print("Nothing to delete!")
        else:
            deleteConsole()
            if config_json == []:
                os.remove("config.json")
            else:
                fw = open('config.json','w')
                json.dump(config_json,fw)
                fw.close()



