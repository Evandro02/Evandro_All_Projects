import random

def Abertura_do_jogo():
    print('\n*************************************')
    print('    Bem vindo no jogo da Forca!    ')
    print('*************************************\n')

def Inserir_palavaras():
    arquivo = open("Palavras.txt","r")
    listas_Palavras = []
    
    for linha in arquivo:
        linha = linha.strip()
        listas_Palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0,len(listas_Palavras))
    palavra_secreta = listas_Palavras[numero].upper()

    return palavra_secreta

def Mensagem_final(acertou, palavra_secreta):
    if(acertou):
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
    else:
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

def main():
    Abertura_do_jogo()
    palavra_secreta = Inserir_palavaras()

    enforcou = False
    acertou = False
    tentativas = 0

    letras_acertadas = ['_' for  letra in palavra_secreta]
    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input('Qual letra? ')
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute.upper() == letra.upper()):
                    letras_acertadas [index] = letra 
                index += 1
        else:
            tentativas += 1
            desenha_forca(tentativas)

        enforcou  = tentativas == 7
        acertou = '_' not in letras_acertadas

        print(letras_acertadas)

    Mensagem_final(acertou, palavra_secreta)
    print('\nGAME OVER')
    

if(__name__ == "__main__"):
    main()