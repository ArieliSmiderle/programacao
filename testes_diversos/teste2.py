#para escolher o jogo
import testes_diversos.teste as teste
import testes_diversos.teste1 as teste1
def escolhe_jogo():
    print('Escolha o seu jogo')
    print('(1)forca, (2)adivinhação')
    jogo = int(input('Qual jogo você deseja jogar: '))
    if(jogo == 1):
        print('Jogando forca')
        teste1.jogar()
    elif (jogo == 2):
        print('Jogando adivinhação')
        teste.jogar()
if (__name__ == "__main__"):
    escolhe_jogo()