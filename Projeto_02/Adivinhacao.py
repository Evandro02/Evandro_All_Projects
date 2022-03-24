import random # Nesse caso usamos para gerar numeros aleitorios 

def jogar():

    print('\n*************************************')
    print('  Bem vindo no jogo de Adivinhação!  ')
    print('*************************************\n')

    numero_secreto = random.randrange (1, 101)
    tentativa = 0
    pontos = 1000


    print('Qual nível de dificuldade? ')
    print('(1) Fácil (2) Médio (3) Difícil')

    nivel = int(input('Define o nível: '))

    if(nivel ==1):
        tentativa = 20
    elif (nivel == 2):
        tentativa = 10
    else:
        tentativa = 5


    for rodada in range(1, tentativa + 1):
        print(f'\nTentativa {rodada} de {tentativa}')
        chute = int (input('Digite um número entre 1 a 100: '))

        if(chute < 1 or chute > 100):
            print('Você deve digitar um número entre 1 a 100!')
            continue

        if(rodada != tentativa):
            if(numero_secreto ==  chute):
                print(f'Você acertou e fez {pontos} pontos')
                break
            else:
                if(chute > numero_secreto):
                    print('Você errou! o seu chute foi maior que o numero secreto.')
                else:
                    print('Você errou! o seu chute foi menor que o numero secreto. ')
                pontos_perdidos = abs(numero_secreto - chute) # Função "abs" deixa os numeros sempre positivos
                pontos = pontos - pontos_perdidos
        else:
            print('\nAcabou as tentativas e você não acertou')

    print('\nGAME OVER')

if(__name__ == "__main__"): # Possamos roda o arquivo independentemente do arquivo jogos
    jogar()