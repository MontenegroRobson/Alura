def jogar():

    print("*" * 35)
    print("****Bem vindo ao jogo de forca!****")
    print("*" * 35)

    palavra_secreta = "banana"

    print("A palavra secreta tem ", len(palavra_secreta), " letras")
    letras_certas = ["_", "_", "_", "_", "_", "_"]
    print(letras_certas)
    
    enforcou = False
    acertou = False

    while(not enforcou and not acertou):
        print()
        chute = input("Digite uma letra: ").lower().strip()

        posicao = 0
        for letra in palavra_secreta:
            if(chute == letra):
                letras_certas[posicao] = chute
            posicao += 1

        print(letras_certas)

    print ("Fim do jogo!")

if (__name__ == "__main__"):
    jogar()