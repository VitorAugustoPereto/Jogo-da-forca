import os

def reiniciar_tela ():
    os.system ("cls")

def menu_inicial():
    print('''
                 ╔╗ ╔═══╗ ╔═══╗ ╔═══╗    ╔═══╗ ╔═══╗     ╔═══╗ ╔═══╗ ╔═══╗ ╔═══╗ ╔═══╗
                 ║║ ║╔═╗║ ║╔═╗║ ║╔═╗║    ╚╗╔╗║ ║╔═╗║     ║╔══╝ ║╔═╗║ ║╔═╗║ ║╔═╗║ ║╔═╗║
                 ║║ ║║ ║║ ║║ ╚╝ ║║ ║║     ║║║║ ║║ ║║     ║╚══╗ ║║ ║║ ║╚═╝║ ║║ ╚╝ ║║ ║║
               ╔╗║║ ║║ ║║ ║║╔═╗ ║║ ║║     ║║║║ ║╚═╝║     ║╔══╝ ║║ ║║ ║╔╗╔╝ ║║ ╔╗ ║╚═╝║
               ║╚╝║ ║╚═╝║ ║╚╩═║ ║╚═╝║    ╔╝╚╝║ ║╔═╗║    ╔╝╚╗   ║╚═╝║ ║║║╚╗ ║╚═╝║ ║╔═╗║
               ╚══╝ ╚═══╝ ╚═══╝ ╚═══╝    ╚═══╝ ╚╝ ╚╝    ╚══╝   ╚═══╝ ╚╝╚═╝ ╚═══╝ ╚╝ ╚╝

                              +====================================+
                             || DEVELOPERS: TAINAN, VITOR, JUNIOR  ||
                              +====================================+ 

Obs: Por gentileza, não use a palavra 'PARALELEPíPEDO',ta muito manjada já.
Tente não dar dicas logícas, exemplo a palavra escondida é "CAMA", pelo amor de Deus,\nnão vá por de dica 'onde a pessoa dorme', larga de ser burro!\n
Obrigado pela compeenção <3 

--------------------------------------------------------------------------------''')

def ganhou():
    print('''
      ╔═══╗ ╔═══╗ ╔═══╗ ╔═══╗ ╔════╗ ╔═══╗    ╔═╗╔═╗ ╔══╗ ╔════╗ ╔═══╗ ╔═══╗ ╔═══╗ ╔╗  ╔╗ ╔══╗
      ║╔═╗║ ║╔═╗║ ║╔══╝ ║╔═╗║ ║╔╗╔╗║ ║╔═╗║    ║║╚╝║║ ╚╣╠╝ ╚══╗ ║ ║╔══╝ ║╔═╗║ ║╔═╗║ ║╚╗╔╝║ ╚╣╠╝
      ║║ ║║ ║║ ╚╝ ║╚══╗ ║╚═╝║ ╚╝║║╚╝ ║║ ║║    ║╔╗╔╗║  ║║    ╔╝╔╝ ║╚══╗ ║╚═╝║ ║║ ║║ ╚╗║║╔╝  ║║
      ║╚═╝║ ║║ ╔╗ ║╔══╝ ║╔╗╔╝   ║║   ║║ ║║    ║║║║║║  ║║   ╔╝╔╝  ║╔══╝ ║╔╗╔╝ ║╚═╝║  ║╚╝║   ║║ 
      ║╔═╗║ ║╚═╝║ ║╚══╗ ║║║╚╗  ╔╝╚╗  ║╚═╝║    ║║║║║║ ╔╣╠╗ ╔╝ ╚═╗ ║╚══╗ ║║║╚╗ ║╔═╗║  ╚╗╔╝  ╔╣╠╗
      ╚╝ ╚╝ ╚═══╝ ╚═══╝ ╚╝╚═╝  ╚══╝  ╚═══╝    ╚╝╚╝╚╝ ╚══╝ ╚════╝ ╚═══╝ ╚╝╚═╝ ╚╝ ╚╝   ╚╝   ╚══╝
                            
                                   ░░░░░░░░░░░░░▄▄▄▄▄▄▄░░░░░░░░░
                                   ░░░░░░░░░▄▀▀▀░░░░░░░▀▄░░░░░░░
                                   ░░░░░░░▄▀░░░░░░░░░░░░▀▄░░░░░░
                                   ░░░░░░▄▀░░░░░░░░░░▄▀▀▄▀▄░░░░░
                                   ░░░░▄▀░░░░░░░░░░▄▀░░██▄▀▄░░░░
                                   ░░░▄▀░░▄▀▀▀▄░░░░█░░░▀▀░█▀▄░░░
                                   ░░░█░░█▄▄░░░█░░░▀▄░░░░░▐░█░░░
                                   ░░▐▌░░█▀▀░░▄▀░░░░░▀▄▄▄▄▀░░█░░
                                   ░░▐▌░░█░░░▄▀░░░░░░░░░░░░░░█░░
                                   ░░▐▌░░░▀▀▀░░░░░░░░░░░░░░░░▐▌░
                                   ░░▐▌░░░░░░░░░░░░░░░▄░░░░░░▐▌░
                                   ░░▐▌░░░░░░░░░▄░░░░░█░░░░░░▐▌░
                                   ░░░█░░░░░░░░░▀█▄░░▄█░░░░░░▐▌░
                                   ░░░▐▌░░░░░░░░░░▀▀▀▀░░░░░░░▐▌░
                                   ░░░░█░░░░░░░░░░░░░░░░░░░░░█░░
                                   ░░░░░█░░▀░░░░░░░░░░░░░░░░▀░░░

''')

def perdeu():

    print('''
                    ╔═══╗ ╔═══╗ ╔═╗╔═╗ ╔═══╗     ╔═══╗ ╔╗  ╔╗ ╔═══╗ ╔═══╗
                    ║╔═╗║ ║╔═╗║ ║║╚╝║║ ║╔══╝     ║╔═╗║ ║╚╗╔╝║ ║╔══╝ ║╔═╗║
                    ║║ ╚╝ ║║ ║║ ║╔╗╔╗║ ║╚══╗     ║║ ║║ ╚╗║║╔╝ ║╚══╗ ║╚═╝║
                    ║║╔═╗ ║╚═╝║ ║║║║║║ ║╔══╝     ║║ ║║  ║╚╝║  ║╔══╝ ║╔╗╔╝
                    ║╚╩═║ ║╔═╗║ ║║║║║║ ║╚══╗     ║╚═╝║  ╚╗╔╝  ║╚══╗ ║║║╚╗
                    ╚═══╝ ╚╝ ╚╝ ╚╝╚╝╚╝ ╚═══╝     ╚═══╝   ╚╝   ╚═══╝ ╚╝╚═╝
                                 ███████████████████████████
                                 ████▀░░░░░░░░░░░░░░░░░▀████
                                 ███│░░░░░░░░░░░░░░░░░░░│███
                                 ██▌│░░░░░░░░░░░░░░░░░░░│▐██
                                 ██░└┐░░░░░░░░░░░░░░░░░┌┘░██
                                 ██░░└┐░░░░░░░░░░░░░░░┌┘░░██
                                 ██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
                                 ██▌░│██████▌░░░▐██████│░▐██
                                 ███░│▐███▀▀░░▄░░▀▀███▌│░███
                                 ██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
                                 ██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
                                 ████▄─┘██▌░░░░░░░▐██└─▄████
                                 █████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
                                 ████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
                                 █████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
                                 ███████▄░░░░░░░░░░░▄███████
                                 ███████████████████████████
''')

