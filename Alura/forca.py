import random

def jogar():
    imprime_mensagem_abertura()

    enforcou = False
    acertou = False
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = ["_" for letra in palavra_secreta]
    chutes_corretos = []
    erros = 0

    print("A palavra tem {} letras".format(len(palavra_secreta)))
    print(letras_acertadas)


    while(not enforcou and not acertou):

        chute = pede_chute(chutes_corretos)
        
        if(chute in palavra_secreta and chute != ""):
            marca_chute_correto(chute, palavra_secreta, letras_acertadas)
            chutes_corretos.append(chute)
        else:
            erros+=1
            desenha_forca(erros)
        enforcou = erros == 7
        acertou = "_" not in letras_acertadas

        if(acertou):
            imprime_mensagem_vencedor(palavra_secreta)
        if(enforcou):
            imprime_mensagem_perdedor(palavra_secreta)


def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def quantidade_de_letras(palavra_secreta):
    return ["_" for letra in palavra_secreta]

def carrega_palavra_secreta():    
    arquivo = open("palavras.txt")
    
    palavras = []

    for linha in arquivo:
        palavras.append(linha.strip().upper())

    numero = random.randrange(0, len(palavras))
    arquivo.close()
    palavra_secreta = palavras[numero]

    return palavra_secreta

def pede_chute(chutes_corretos):
    chute = str(input("Qual letra:\n"))
    chute = chute.strip().upper()  

    if(chute in chutes_corretos):
        print("Letra ja marcada!")
    
    return chute

def marca_chute_correto(chute, palavra_secreta, letras_acertadas):
    
        index = 0
        for letra in palavra_secreta:
            if(chute == letra):
                letras_acertadas[index] = letra
            index = index + 1

        print(letras_acertadas)

def imprime_mensagem_vencedor(palavra_secreta):
    print("Parabéns, você ganhou!")
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

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
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