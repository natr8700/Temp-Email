import os
from colorama import Fore
from mailtm import Email
os.system("cls")
def temp_mail(message):
    print("\nSubject: " + message['subject'])
    print("Content: " + message['text'] if message['text'] else message['html'])
tempmail = Email()
print(Fore.RED + 
"""
 _____                           _____                    _  _ 
|_   _|                         |  ___|                  (_)| |
  | |    ___  _ __ ___   _ __   | |__   _ __ ___    __ _  _ | |
  | |   / _ \| '_ ` _ \ | '_ \  |  __| | '_ ` _ \  / _` || || |
  | |  |  __/| | | | | || |_) | | |___ | | | | | || (_| || || |
  \_/   \___||_| |_| |_|| .__/  \____/ |_| |_| |_| \__,_||_||_|
                        | |                                    
                        |_|                                    
""")
tempmail.register()
print(Fore.BLUE + "\nEmail Adress: " + str(tempmail.address))
tempmail.start(temp_mail, interval=1)
print(Fore.GREEN + "\nWaiting for new email . . .")