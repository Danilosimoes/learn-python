import math

'''
idade = int(input('Qual a sua Idade?: '))
altura = float(input('Qual a sua Altura?: '))
peso = float(input('Qual o seu peso?: '))

if idade >= 18 and altura >= 1.70 and peso >= 70:
    print('Você está apto para entrar no Exército!')
else:
    print('Você não está apto para entrar no Exército!')
    
'''


def join_army(age, height, weight):
    age = float(age)
    height = float(height)
    weight = float(weight)

    if age >= 18 and height >= 1.70 and weight >= 70:
        return "You can to join the army"
    else:
        return "You can't to join the army"


if __name__ == '__main__':
    age = input('Type your age: ')
    height = input('Type your height: ')
    weight = input('Type your weight: ')
    data = join_army(age, height, weight)
    print(data)
