from random import randint

itens = ['Pedra', 'Papel', 'Tesoura']

computador = randint(0, 2)
print('''SUAS OPÇÕES 
[ 0 ]
[ 1 ]
[ 2 ]''')
print('-+' * 20)

try:
    jogador = int(input('Qual a sua jogada: '))
except ValueError:
    print('Digite um número inteiro, entre 0 e 2!!')
else:

    try:
        print('-+' * 20)
        print(f'O jogador jogou {(itens[jogador])}')
    except IndexError:
        print(f'Erro: Número incorreto')
    else:
        print(f'O computador jogou {(itens[computador])}')

    if computador == 0:
        if jogador == 0:
            print('Empate!!')
        elif jogador == 1:
            print('O Jogador ganhou!!')
        elif jogador == 2:
            print('Computador ganhou!!')
    elif computador == 1:
        if jogador == 0:
            print('Computador ganhou!!')
        elif jogador == 1:
            print('Empate!!')
        elif jogador == 2:
            print('Jogador ganhou!!')
    elif computador == 2:
        if jogador == 0:
            print('Jogador ganhou!!')
        elif jogador == 1:
            print('Computador ganhou!')
        elif jogador == 2:
            print('Empate!!')

    try:
        print('=+'*20)
        print(f'O jogador jogou {(itens[jogador])} e o computador {(itens[computador])}')
    except IndexError:
        print('Jogada Inválida')

