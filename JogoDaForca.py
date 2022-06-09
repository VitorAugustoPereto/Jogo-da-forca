from funcoes import reiniciar_tela, menu_inicial, ganhou, perdeu
import time

reiniciar_tela()
menu_inicial()
time.sleep(12)
reiniciar_tela()

desafiante = str(input('Digite o nome do DESAFIANTE: '))
desafiado = str(input('\nDigite o nome do DESAFIADO: '))

reiniciar_tela()

print('\nAs seguintes informações devem ser completadas pelo DESAFIANTE: ')
palavra_chave = str(input('\nDigite a palavra que você queira inserir na forca: ')).lower().strip()
dica1 = input('\nDigite a primeira dica para seu adversário: ')
dica2 = input('\nDigite a segunda dica para seu adversário: ')
dica3 = input('\nDigite a terceira dica dica para seu adversário: ')

letras_digitadas = []
erros = 0
letras_certas = []
reiniciar_tela()

palavra_escondida = ''
palavra_escondida = palavra_escondida * len(palavra_chave)
print("Bem Vindo", desafiado)
print('\nA palavra escolhida por', desafiante, 'é:', palavra_escondida)

while True:
    key = ''
    for letra in palavra_chave:
        key += letra if letra in letras_certas else "_ "
    print(key)
    if key == palavra_chave:
        ganhou()
        break
    print('''\nDigite "0" para usar as dicas''')
    tentativa = input("\nDigite uma letra: ").lower().strip()
    reiniciar_tela()
    if tentativa == '0':
        escolher_dica = input('''
(1) Para usar a primeira dica.
(2) Para usar a segunda dica.
(3) Para usar a terceira dica.

Selecione uma opção: ''')
        if escolher_dica == "1":
            print('\nDica 1: ', dica1)
            time.sleep(5)
            reiniciar_tela()
        elif escolher_dica == '2':
            print('\nDica 2: ', dica2)
            time.sleep(5)
            reiniciar_tela()
        elif escolher_dica == '3':
            print('\nDica 3: ', dica3)
            time.sleep(5)
            reiniciar_tela()
        else:
            print("Opção inválida!\n")
            time.sleep(3)
            reiniciar_tela()
    try:
        letras_digitadas
    except:
        print("Caracter inválido!\n")

    if tentativa in letras_digitadas:
        print("Você já chutou essa letra!\n")
    else:
        letras_digitadas += tentativa

    if tentativa in palavra_chave or tentativa == '0':
        letras_certas += tentativa
    else:
        erros += 1
        print("Essa letra não está na palavra!\n")

    if erros >= 6:
        print('''Game Over !!!\n
    |==========
    |    |     Essa vida foi perdida por sua causa!
    |    0     1 minuto de silêncio em respeito a essa vítima...
    |   /|\    Partiu matar mais um?  :D
    |   / \    
    ===========
    ''')
        break

    print('|===========\n|    |')
    print("|    0   " if erros >= 1 else '|')
    linha2 = ""
    if erros == 2:
        linha2 = "    |   "
    elif erros == 3:
        linha2 = "   /|   "
    elif erros >= 4:
        linha2 = "   /|\ "
    print("|%s" % linha2)
    linha3 = ""
    if erros == 5:
        linha3 = "   /     "
    elif erros >= 6:
        linha3 = "   / \ "
    print("|%s" % linha3)
    print("|\n===========")
    if erros == 6:
        print("Ai que burro, da zero pra ele!")
        break
reiniciar_tela()
if key == palavra_chave:
    ganhou()
    time.sleep(3)
    reiniciar_tela()
else:
    perdeu()
    time.sleep(3)
    reiniciar_tela()
registro = open("registro.txt", "w")
registro.write("A Palavra chave era: %s \n" % palavra_chave)

if key == palavra_chave:
    registro.write("O Vencedor foi...: %s \n" % desafiado)
else:
    registro.write("O Vencedor foi...: %s \n" % desafiante)

registro = open("registro.txt", "r")
conteudo = registro.read()
print(conteudo)
