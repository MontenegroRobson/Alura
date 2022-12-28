from random import randint

def jogar():

    print("*" * 35)
    print("Bem vindo ao jogo de adivinhação!")
    print("*" * 35)

    número_secreto = randint(1, 100)
    pontos = 1000

    while(True):
        chute   = int(input("Digite o seu palpite entre 1 e 100: "))
        if (chute < 1 or chute > 100):
            print("Digite um número válido: ")
            continue
        acertou = chute == número_secreto
        maior   = chute >  número_secreto

        if(acertou):
            print(f"Parabéns, você acertou e fez {pontos} pontos!")
            break
        else:
            if(maior):
                print("Que pena! Você errou. É um número menor. Tente de novo")
                pontos_perdidos = abs(número_secreto - chute)
                pontos-= pontos_perdidos
            else:
                print("Que pena! Você errou. É um número maior. Tente de novo")
                pontos_perdidos = abs(número_secreto - chute)
                pontos-= pontos_perdidos

if (__name__ == '__main__'):
    jogar()