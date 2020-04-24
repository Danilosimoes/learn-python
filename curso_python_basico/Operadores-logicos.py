import math


idade = int(input('Qual a sua Idade?: '))
altura = float(input('Qual a sua Altura?: '))
peso = float(input('Qual o seu peso?: '))

if idade >= 18 and altura >= 1.70 and peso >= 70:
    print('Você está apto para entrar no Exército!')
else:
    print('Você não está apto para entrar no Exército!')