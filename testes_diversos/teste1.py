import random

def jogar():

    imprime_mensagem_abertura()
    palavra = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while(not acertou and not enforcou):

        chute = pede_chute()

        if (chute in palavra):
            marca_chute_correto(chute, letras_acertadas, palavra)
        else:
            erros += 1
            desenha_forca(erros)
        
        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        imprime_mensagem_vencendor()
    else:
        imprime_mensagem_perdedor(palavra)

    print('fim de jogo')

def imprime_mensagem_abertura():
    print("Bem vindo ao jogo da forca")

def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    
    numero = random.randrange(0, len(palavras))
    palavra = palavras[numero].upper()
    return palavra

def inicializa_letras_acertadas(palavra):
    return["_" for letra in palavra]

def pede_chute():
    chute = input('Digite uma letra: ')
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute, letras_acertadas, palavra):
    index = 0
    for letra in palavra:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1
def imprime_mensagem_vencendor():
    print ("Você ganhou o jogo")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra):
    print("Você foi enforcado")
    print("a palavra era {}".format(palavra))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "__main__"):
    jogar()
