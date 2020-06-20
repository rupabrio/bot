from sys import argv

from utils.menu import *

from engine import instablot

if __name__ == '__main__':
    # Menu de entrada
    arguments = argv[1:]
    show_banner()
    print(arguments)
