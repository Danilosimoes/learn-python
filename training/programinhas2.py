from random import randint, choice
from time import sleep

p = 'par'
i = 'impar'
p_i = [p, i]
escolha = choice(p_i)
i.lower()
p.lower()
print(f'A escoha do computador foi: {escolha} ')
voce = str(input('Escolha par ou impar: '))

computador = randint(0, 100)
escolhido = computador

num = int(input('Escolha um número: '))
print(f'O computador jogou: {escolhido} ')

print('PAR OU IMPAR')

print('PROCESSANDO...')
sleep(1)

numero = computador
p_ou_i = escolhido + num
resultado = p_ou_i % 2

if resultado == 0 and escolha == 'par':
    print(f'O {p_ou_i} é par e o computador ganhou!!!')
elif resultado == 0 and voce == 'par':
    print(f'O {p_ou_i} é par e voce ganhou!!!')
elif escolha == 'impar':
    print(f'O {p_ou_i} é ímpar e o computador ganhou')
elif voce == 'impar':
    print(f'O {p_ou_i} é impar voce ganhou')
else:
    print('Operacao invalida')
