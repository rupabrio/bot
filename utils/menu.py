def show_banner():
    import os
    try:
        os.system('cls')
    except:
        os.system('clear')
    finally:
        pass

    banner = r"""
++++++++++++++++++++++++++++++++++++++++++++++
BIENVENIDO AMO! COMO PUEDO AYUDARTE ~
       _______                   ________    |
      |ooooooo|      ____       | __  __ |   |
      |[]+++[]|     [____]      |/  \/  \|   |
      |+ ___ +|    ](<><>)[      |\__/\__/|   |
      |:|   |:|   ___\__/___    |[][][][]|   |
      |:|___|:|  |__|    |__|   |++++++++|   |
      |[]===[]|   |_|_/\_|_|    | ______ |   |
    _ ||||||||| _ | | __ | | __ ||______|| __|
      |_______|   |_|[::]|_|    |________|   \
                  \_|_||_|_/                  \
+++++++++++++++++++++++++++++++++++++++++++++++
    """
    print(banner)
