import json
import os

config_json = []

# i18n
LANG_LIST = ["en", "ja"]
if not os.path.exists("./lang/lang.txt"):
    lang = input("Which language? (English=en, 日本語=ja): ")
    if not lang in LANG_LIST:
        print("Invalid lang / 無効な言語です")
        exit()
    with open("./lang/lang.txt", "w", encoding="utf-8") as f:
        f.write(lang)
else:
    with open("./lang/lang.txt", "r", encoding="utf-8") as f:
        lang = f.read()


message = {}
with open(f'./lang/{lang}.json', "r", encoding="utf-8") as f:
    message = json.load(f)


def delete_console():
    global config_json
    global message

    cnt = 0
    print("-" * 30)
    for settings in config_json:
        if settings["console"] == 4:
            cname = settings["custom"]
        else:
            cname = console_names[settings["console"]]
        print("[%d]%-15s IP %s" % (cnt, cname, settings["ip"]))
        cnt += 1
    print("-" * 30)
    end_code = cnt
    delete_num = -1
    while not 0 <= delete_num <= end_code:
        print(message["delete_console"].format(end_code, end_code))
        delete_num = int(input())
    if delete_num == end_code:
        return
    config_json.pop(delete_num)
    print(message["deleted"])


def add_new_console():
    global message

    console = 100
    while not 0 <= console <= 4:
        print(message["add_console"])
        console = int(input())
    jsonar = {"console": console}
    if console == 4:
        print(message["type_console_name"])
        jsonar.update({"custom": input()})
    print(message["type_console_ip"])
    jsonar.update({"ip": input()})
    return jsonar


if not os.path.exists("config.json"):
    config_json = []
else:
    f = open("config.json", "r")
    config_json = json.load(f)
    f.close()
console_names = ["Nintendo Switch", "Nintendo 3DS", "Play Station 3", "Play Station 4"]
while True:
    if config_json:
        print("-" * 30)
        for settings in config_json:
            if settings["console"] == 4:
                cname = settings["custom"]
            else:
                cname = console_names[settings["console"]]
            print("[%-15s] IP %s" % (cname, settings["ip"]))
        print("-" * 30)
    setting_option = 100
    while not 0 <= setting_option <= 2:
        print(message["config_main_menu"])
        setting_option = int(input())
    if setting_option == 2:
        print(message["goodby"])
        exit()

    if setting_option == 0:
        eachArray = add_new_console()
        config_json.append(eachArray)
        fw = open("config.json", "w")
        json.dump(config_json, fw)
        fw.close()
        print(message["added"])

    if setting_option == 1:
        if not config_json:
            print(message["console_not_found"])
        else:
            delete_console()
            if not config_json:
                os.remove("config.json")
            else:
                fw = open("config.json", "w")
                json.dump(config_json, fw)
                fw.close()
