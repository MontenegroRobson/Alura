import forca
import adivinhacao

def escolha_jogo():
    print("*" * 35)
    print("********Escolha o seu jogo!********")
    print("*" * 35)

    print("[1] - Forca \n[2] - Adivinhação ")

    jogo = int(input("Escolha o jogo: "))

    if (jogo == 1):
        print("Jogando Forca")
        forca.jogar()
    elif (jogo == 2):
        print("Jogando Adivinhação")
        adivinhacao.jogar()
    else:
        print("opção inválida!")

if(__name__ == '__main__'):
    escolha_jogo()
