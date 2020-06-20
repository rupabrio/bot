from sys import argv

from utils.menu import *

from engine import bots

mi_objetivo_de_clase = bots.Bot()

if __name__ == '__main__':
    # Menu de entrada
    arguments = argv[1:]
    show_banner()
    print(arguments)
