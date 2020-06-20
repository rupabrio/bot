from sys import argv

from utils.menu import *

from engine import bots

if __name__ == '__main__':
    # Menu de entrada
    menu = """1. Log in | 2. Go to user | 3. Exit"""
    arguments = argv[1:]
    show_banner()
    print("Press Enter to Start Bot, Press CTR C to cancel")
    input("GO?")
    uname = input("username=> ")
    pw = input("passwd=> ")
    my_bot = bots.Bot(uname, pw)
    while True:
        print(menu)
        option = input("=> ")
        if option not in ["1", "2", "3"]:
            print("Not valid")
            continue
        elif option == "1":
            try:
                my_bot.enter()
            except:
                print("Oops something happened!")

        elif option == "2":
            target = input("Type the name of target user=> ")
            my_bot.go_to(user=target)

        elif option == "3":
            print("Goodbye")
            my_bot.exit()
            break
