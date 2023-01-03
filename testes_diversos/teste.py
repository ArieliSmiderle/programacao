import random
def jogar():
    total_tentativas = 0
    pontos = 1000
    numero_secreto = random.randrange(1, 101)
    print("Bem vindo ao jogo de adivinhação")
    print("Escolha seu nível de dificuldade")
    print("(1)fácil, (2)médio, (3)difícil")
    nivel = int(input("Defina o nível: "))
    if (nivel == 1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5
    for rodada in range (1, total_tentativas + 1):
        print('Tentativa {} de {}'.format(rodada, total_tentativas))
        chute = int(input('Digite o número entre 1 e 100: '))
        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto
        if (chute < 1 or chute > 100):
            print('Digite um número entre 0 e 100')
            continue
        if (acertou):
            print('Parabéns, você acertou e fez {} pontos!'.format(pontos))
            break
        else:
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            if (maior):
                print ('O número é menor que {}'.format(chute))
                if(rodada == total_tentativas):
                    print("O número secreto era {} e você fez {} pontos".format(numero_secreto, pontos))
            elif (menor):
                print('O número é maior que {}'.format(chute))
                if(rodada == total_tentativas):
                    print("O número secreto era {} e você fez {} pontos".format(numero_secreto, pontos))
    print('Fim do jogo')


if(__name__ == "__main__"):
    jogar()