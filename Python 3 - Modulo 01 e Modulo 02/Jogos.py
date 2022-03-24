import Forca
import Adivinhacao

print('\n*************************************')
print('        Escolha o seu jogo!         ')
print('*************************************\n')

print('(1) Forca  \n(2) Adivinhação')

jogo = int(input ("\nQual jogo? "))

if(jogo == 1):
    print('Jogo da Forca')
    Forca.main()
elif(jogo == 2):
    print('Jogo de Adivinhação')
    Adivinhacao.jogar()