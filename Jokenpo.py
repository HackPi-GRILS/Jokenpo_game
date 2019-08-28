from time import sleep
from random import randint
partidas = ganhou = 0
while True:
    print('''Suas opções:
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA''')
    itens = ('Pedra', 'Papel', 'Tesoura')
    jogador = int(input('Qual sua jogada? '))
    computador = randint(0,2)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!!!')
    print('-='*15)
    print('\033[32mComputador jogou {}'.format(itens[computador]))
    print('\033[34mJogador jogou {}\033[m'.format(itens[jogador]))
    print('-='*15)
    if jogador != computador:
        if jogador == 0 and computador == 1:
            print('Você perdeu!')
        elif jogador ==0 and computador == 2:
            print('Você VENCEU!')
            ganhou += 1
        elif jogador == 1 and computador == 0:
            print('você VENCEU!')
            ganhou += 1
        elif jogador == 1 and computador == 2:
            print('você PERDEU! ')
        elif jogador == 2 and computador == 0:
            print('você PERDEU!')
        else:
            print('você VENCEU!')
            ganhou += 1
    else:
        print('EMPATE')
        partidas =+ 1
    pergunta = (str(input('Quer continuar no jogo: [S/N]'))).strip().upper()
    if pergunta == 'S':
        print('-'*25)
        print('VAMOS JOGAR OUTRA PARTDA')
        print('-'*25)
        partidas += 1
    else:
        break
print('Obrigado por ter jogado comigo!!!')
print('No total de {} partidas você ganhou {}'.format(partidas, ganhou))
